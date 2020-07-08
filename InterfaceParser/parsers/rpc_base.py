"""RPC XML base parser.

Contains base parser for SDLRPC v1/v2 and JSON RPC XML format.

"""
import logging
import re
from abc import ABC, abstractmethod
from collections import OrderedDict
from xml.etree import ElementTree

from model.array import Array
from model.boolean import Boolean
from model.enum import Enum
from model.enum_element import EnumElement
from model.enum_subset import EnumSubset
from model.float import Float
from model.function import Function
from model.integer import Integer
from model.interface import Interface
from model.issue import Issue
from model.param import Param
from model.string import String
from model.struct import Struct
from parsers.parse_error import ParseError


class RPCBase(ABC):
    """RPC XML Parser base.

    This class must not be used directly. One of its subclasses must be used instead.

    """

    def __init__(self):
        """Constructor."""
        self._types = {}
        self._enums = OrderedDict()
        self._structs = OrderedDict()
        self._functions = OrderedDict()
        self._params = {}
        self.logger = logging.getLogger('RPCBase')

    @property
    @abstractmethod
    def get_version(self):
        """Must be overridden in child instances
        :return: current version of Parser
        """

    def parse(self, filename):
        """Parse XML.

        Returns an instance of model.Interface containing parsed
        interface or raises ParseError if input XML contains errors
        and can't be parsed.

        :param filename: name of input XML file.
        :return: Interface object
        """

        tree = ElementTree.parse(filename)
        root = tree.getroot()

        self._enums = self._initialize_enums()
        self._structs = OrderedDict()
        self._functions = OrderedDict()
        self._params = {}

        self._types = dict(self._enums.items())

        self._parse_root(root)

        return Interface(enums=self._enums, structs=self._structs,
                         functions=self._functions, params=self._params)

    @staticmethod
    def _initialize_enums():
        """Initialize enums.

        Required for formats where these enums must be generated automatically
        according to the declared in the XML functions.

        These enums are filled during the parsing of the functions.

        :return: an OrderedDict with two empty enums: "FunctionID" and "messageType".
        """
        return OrderedDict(
            [("FunctionID", Enum(name="FunctionID")),
             ("messageType", Enum(name="messageType"))])

    def _check_function_param_name(self, function_param_name):
        """Check function param name.

        This method is called to check whether the newly parsed function
        parameter name conflicts with some predefined name.

        This implementation doesn't check anything because there is no
        predefined names in base RPC XML.

        :param function_param_name: string with function name
        """

    def _parse_root(self, root):
        """Parse root XML element.

        Default implementation parses root as interface element without a prefix.

        :param root: ElementTree root Element object
        """

        self._parse_interface(root, "")

    def _parse_interface(self, interface, prefix):
        """Parse interface element.

        :param interface: interface element.
        :param prefix: string prefix for all types of the interface.
        """
        if interface.tag != "interface":
            raise ParseError("Invalid interface tag: " + interface.tag)

        params, subelements, attrib = self._parse_base_item(interface, "")

        for param in ["description", "design_description", "todos"]:
            if len(params[param]) != 0:
                attrib[param] = "\n".join(params[param])

        if len(params['issues']) != 0:
            attrib["issues"] = "\n".join(i.value for i in params["issues"])

        self._params.update({prefix + k: v for k, v in attrib.items()})

        for element in subelements:
            if element.tag == "enum":
                enum = self._parse_enum(element, prefix)
                self._evaluate_element(self._enums, enum)
                self._add_type(enum)
            elif element.tag == "struct":
                struct = self._parse_struct(element, prefix)
                self._evaluate_element(self._structs, struct)
                self._add_type(struct)
            elif element.tag == "function":
                func = self._parse_function(element, prefix)
                self._evaluate_element(self._functions, func, (func.function_id, func.message_type))
            else:
                raise ParseError("Unexpected element: " + element.tag)

    @staticmethod
    def _evaluate_element(items, item, key=None):
        """Add new item in the items dictionary with given key.

        Performs additional check for presence in the dictionary and throws
        ParseError exception if key already exist.

        :param items: OrderedDict with already parsed EnumElement object
        :param item: EnumElement object
        :param key: None
        """
        if key is None:
            key = item.name

        if key in items:
            raise ParseError("{} '{}' is declared more than once".format(type(item).__name__, key))
        items[key] = item

    def _add_type(self, _type):
        """Add new type in the internal types dictionary.

        Performs additional check for presence type with same name in the
        dictionary and throws ParseError exception if key already exist.

        :param _type: Struct or Enum object
        """
        if _type.name in self._types:
            raise ParseError("Type '{}' is declared as both struct and enum".format(_type.name))

        self._types[_type.name] = _type

    def _parse_enum(self, element, prefix):
        """Parse element as enumeration.

        :param element: an instance of Element (from ElementTree)
        :param prefix: empty string
        :return: an instance of model.Enum
        """
        params, subelements, attrib = self._parse_base_item(element, prefix)

        for attribute in attrib:
            if attribute in ["internal_scope", "scope", "deprecated", "removed"]:
                params[attribute] = attrib[attribute]
            elif attribute in ["since", "until"]:
                params[attribute] = self._parse_version(attrib[attribute])
            else:
                raise ParseError("Unexpected attribute '{}' in enum '{}'".format(attribute, params["name"]))

        elements = OrderedDict()
        for subelement in subelements:
            if subelement.tag == "element":
                self._evaluate_element(elements, self._parse_enum_element(subelement))
            else:
                raise ParseError("Unexpected element '{}' in enum '{}'".format(subelement.tag, params["name"]))
        params["elements"] = elements

        return Enum(**params)

    def _parse_struct(self, element, prefix):
        """Parse element as structure.

        :param element: an instance of Element (from ElementTree)
        :param prefix: empty string
        :return: an instance of model.Struct
        """
        params, subelements, attrib = self._parse_base_item(element, prefix)
        """
        Create an empty object for new type to types collection.
        This is needed for parser to apply type for struct members
        that consist of its own type.
        E.g.:
            struct VideoStreamingCapability {
            ...
            VideoStreamingCapability additionalVideoStreamingCapabilities[]
            }
        """
        struct = Struct(**params)
        self._add_type(struct)

        for attribute in attrib:
            if attribute in ["scope", "deprecated", "removed"]:
                params[attribute] = attrib[attribute]
            elif attribute in ["since", "until"]:
                params[attribute] = self._parse_version(attrib[attribute])
            else:
                raise ParseError("Unexpected attribute '{}' in struct '{}'".format(attribute, params["name"]))

        members = OrderedDict()
        for subelement in subelements:
            if subelement.tag == "param":
                self._evaluate_element(members, self._parse_struct_param(subelement, prefix))
            else:
                raise ParseError("Unexpected subelement '{}' in struct '{}'".format(subelement.name, params["name"]))
        params["members"] = members

        """
        Remove empty object for new type to prevent errors of adding such type twice (see self._add_type).
        After return statement of current method is done the new type with all its params
        will be added into types collection.
        """
        self._types.pop(struct.name, None)

        return Struct(**params)

    def _parse_function(self, element, prefix):
        """Parse element as function.

        :param element: an instance of Element (from ElementTree)
        :param prefix: empty string
        :return: an instance of model.Function
        """
        params, subelements, attrib = self._parse_base_item(element, prefix)

        function_id, message_type = self._parse_function_id_type(params["name"], attrib)
        params["function_id"] = function_id
        params["message_type"] = message_type

        for attribute in attrib:
            if attribute in ["scope", "deprecated", "removed"]:
                params[attribute] = attrib[attribute]
            if attribute in ["since", "until"]:
                params[attribute] = self._parse_version(attrib[attribute])

        function_params = OrderedDict()
        for subelement in subelements:
            if subelement.tag == "param":
                function_param = self._parse_function_param(subelement, prefix)
                self._check_function_param_name(function_param.name)
                if function_param.name in function_params:
                    raise ParseError("Parameter '{}' is specified more than once for function '{}'"
                                     .format(function_param.name, params["name"]))
                function_params[function_param.name] = function_param
            else:
                raise ParseError("Unexpected subelement '{}' in function '{}'".format(subelement.tag, params["name"]))
        params["params"] = function_params

        return Function(**params)

    def _parse_function_id_type(self, function_name, attrib):
        """Parse function id and message type according to XML format.

        This implementation takes function name as function id and extracts
        attribute "messagetype" as message type and searches them in enums
        "FunctionID" and "messageType" adding the missing elements if
        necessary.

        :param function_name: string with function name
        :param attrib: dict with function attributes
        :return: function id and message type as an instances of EnumElement.
        """
        if "messagetype" not in attrib:
            raise ParseError("No messagetype specified for function '{}'".format(function_name))

        function_id = self._provide_enum_element_for_function(
            "FunctionID",
            function_name)

        message_type = self._provide_enum_element_for_function(
            "messageType",
            self._extract_attrib(attrib, "messagetype"))

        return function_id, message_type

    def _provide_enum_element_for_function(self, enum_name, element_name):
        """Provide enum element for functions.

        Search an element in an enum and add it if it is missing.

        :param enum_name: string with enum name
        :param element_name: string with interface name + function name
        :return: an instance of model.EnumElement
        """
        if enum_name not in self._types:
            raise ParseError("Enum '{}' is not initialized".format(enum_name))

        enum = self._types[enum_name]

        if not isinstance(enum, Enum):
            raise ParseError("'{}' is not an enum".format(enum_name))

        if element_name not in enum.elements:
            enum.elements[element_name] = EnumElement(name=element_name)

        return enum.elements[element_name]

    def _parse_base_item(self, element, prefix):
        """Parse element as base item.

        :param element: an instance of Element (from ElementTree)
        :param prefix: empty string
        :return: an params, sub-elements and attributes of the element
        """
        params = {"description": [], "design_description": [], "issues": [], "todos": [], "history": None}

        subelements = []

        if "name" not in element.attrib:
            raise ParseError("Name is not specified for " + element.tag)

        params["name"] = prefix + element.attrib["name"]
        attrib = dict(element.attrib.items())
        del attrib["name"]

        params["platform"] = self._extract_attrib(attrib, "platform")

        for subelement in element:
            if subelement.tag == "description":
                params["description"].append(self._parse_simple_element(subelement))
            elif subelement.tag == "designdescription":
                params["design_description"].append(self._parse_simple_element(subelement))
            elif subelement.tag == "todo":
                params["todos"].append(self._parse_simple_element(subelement))
            elif subelement.tag == "issue":
                params["issues"].append(self._parse_issue(subelement))
            elif subelement.tag == "history":
                if params["history"] is not None:
                    raise ParseError("Elements can only have one history tag: " + element.tag)
                params["history"] = self._parse_history(subelement, prefix, element)
            elif subelement.tag == "warning":
                self._parse_simple_element(subelement)
            else:
                subelements.append(subelement)

        return params, subelements, attrib

    @staticmethod
    def _parse_simple_element(element):
        """Parse element as simple element and returns it's text.

        Element is simple when it contains no subelements and attributes.

        :param element: an instance of Element (from ElementTree)
        :return: element text if present or empty string if not
        """
        if len(element) != 0:
            raise ParseError("Unexpected subelements in '{}'".format(element.tag))
        if len(element.attrib) != 0:
            raise ParseError("Unexpected attributes in '{}'".format(element.tag))
        return element.text if element.text is not None else ""

    @staticmethod
    def _parse_issue(element):
        """Parse element as issue.

        Issue must not contain subelements and attributes.

        :param element: an instance of Element (from ElementTree)
        :return: an instance of model.Issue
        """
        if len(element) != 0:
            raise ParseError("Unexpected subelements in issue")
        if "creator" not in element.attrib:
            raise ParseError("No creator in issue")
        if len(element.attrib) != 1:
            raise ParseError("Unexpected attributes in issue")

        return Issue(
            creator=element.attrib["creator"],
            value=element.text if element.text is not None else "")

    def _parse_enum_element(self, element):
        """Parse element as element of enumeration.

        :param element: an instance of Element (from ElementTree)
        :return: an instance of model.EnumElement
        """
        params, subelements, attrib = self._parse_base_item(element, "")

        if len(subelements) != 0:
            raise ParseError("Unexpected subelements in enum element")

        self._ignore_attribute(attrib, "scope")
        self._ignore_attribute(attrib, "rootscreen")

        for attribute in attrib:
            if attribute == "value":
                try:
                    params[attribute] = int(attrib[attribute])
                except:
                    raise ParseError("Invalid value for enum element: '{}'".format(attrib[attribute]))
            elif attribute == "hexvalue":
                params["hex_value"] = attrib[attribute]
            elif attribute in ["internal_name", "deprecated", "removed"]:
                params[attribute] = attrib[attribute]
            elif attribute in ["since", "until"]:
                params[attribute] = self._parse_version(attrib[attribute])

        return EnumElement(**params)

    def _parse_struct_param(self, element, prefix):
        """Parse element as structure parameter.

        :param element: an instance of Element (from ElementTree)
        :param prefix: empty string
        :return: an instance of model.param
        """
        params, subelements, attrib = self._parse_param_base_item(element, prefix)

        if len(attrib) != 0:
            raise ParseError("Unknown attribute(s) {0} in param {1}".format(attrib, params["name"]))

        if len(subelements) != 0:
            raise ParseError("Unknown subelements in param '{}'".format(params["name"]))

        return Param(**params)

    def _parse_function_param(self, element, prefix):
        """Parse element as function parameter.

        :param element: an instance of Element (from ElementTree)
        :param prefix: empty string
        :return: an instance of model.Param
        """
        params, subelements, attrib = self._parse_param_base_item(element, prefix)

        default_value = None
        default_value_string = self._extract_attrib(attrib, "defvalue")
        if default_value_string is not None:
            param_type = params["param_type"]
            if isinstance(param_type, Boolean):
                default_value = self._get_bool_from_string(default_value_string)
            elif isinstance(param_type, Integer):
                try:
                    default_value = int(default_value_string)
                except:
                    raise ParseError("Invalid value for integer: '{}'".format(default_value_string))
            elif isinstance(param_type, Float):
                try:
                    default_value = float(default_value_string)
                except:
                    raise ParseError("Invalid value for float: '{}'".format(default_value_string))
            elif isinstance(param_type, String):
                default_value = default_value_string
            elif isinstance(param_type, (Enum, EnumSubset)):
                if isinstance(param_type, EnumSubset):
                    allowed_elements = param_type.allowed_elements
                else:
                    allowed_elements = param_type.elements
                if default_value_string not in allowed_elements:
                    raise ParseError("Default value '{}' for parameter '{}' is not a member of {}"
                                     .format(default_value_string, params["name"], type(param_type.__name__)))
                default_value = allowed_elements[default_value_string]
            else:
                raise ParseError("Default value specified for " + type(param_type).__name__)
        params["default_value"] = default_value

        if len(attrib) != 0:
            raise ParseError("Unexpected attributes in parameter '{}'".format(params["name"]))

        if len(subelements) != 0:
            raise ParseError("Unexpected subelements in parameter '{}'".format(params["name"]))

        return Param(**params)

    def _parse_param_base_item(self, element, prefix):
        """Parse base param items.

        :param element: an instance of Element (from ElementTree)
        :param prefix: empty string
        :return: params, other subelements and attributes.
        """
        params, subelements, attrib = self._parse_base_item(element, "")
        params.update(self._extract_all_base_attrib(attrib))

        param_type, default_value = self._extract_param_type(attrib, prefix, params["name"])

        base_type = param_type.element_type if isinstance(param_type, Array) else param_type

        other_subelements = []
        for subelement in subelements:
            if subelement.tag == "element":
                base_type = self._parse_base_enum_element(subelement, base_type, params)
            else:
                other_subelements.append(subelement)

        if isinstance(param_type, Array):
            param_type.element_type = base_type
        else:
            param_type = base_type

        params["param_type"] = param_type
        if default_value is not None:
            params["default_value"] = default_value

        return params, other_subelements, attrib

    def _extract_all_base_attrib(self, attrib):
        params = {}
        since_version = self._extract_attrib(attrib, "since")
        if since_version is not None:
            params["since"] = self._parse_version(since_version)

        until_version = self._extract_attrib(attrib, "until")
        if until_version is not None:
            params["until"] = self._parse_version(until_version)

        deprecated = self._extract_attrib(attrib, "deprecated")
        if deprecated is not None:
            params["deprecated"] = deprecated

        removed = self._extract_attrib(attrib, "removed")
        if removed is not None:
            params["removed"] = removed

        scope = self._extract_attrib(attrib, "scope")
        if scope is not None:
            params["scope"] = scope

        is_mandatory = self._extract_attrib(attrib, "mandatory")
        if is_mandatory is None:
            raise ParseError("'mandatory' is not specified for parameter '{}'".format(params["name"]))

        params["is_mandatory"] = self._get_bool_from_string(is_mandatory)

        return params

    def _extract_param_type(self, attrib, prefix, name):
        type_name = self._extract_attrib(attrib, "type")
        if type_name is None:
            raise ParseError("Type is not specified for parameter '{}'".format(name))
        if type_name == "Boolean":
            default_value = self._extract_attrib(attrib, "defvalue")
            if default_value is not None:
                default_value = self._get_bool_from_string(default_value)
            param_type = Boolean(default_value=default_value)
        elif type_name in ('Integer', 'Float', 'Double'):
            min_value = self._extract_optional_number_attrib(
                attrib, "minvalue", int if type_name == "Integer" else float)
            max_value = self._extract_optional_number_attrib(
                attrib, "maxvalue", int if type_name == "Integer" else float)
            default_value = self._extract_optional_number_attrib(
                attrib, "defvalue", int if type_name == "Integer" else float)

            param_type = (Integer if type_name == "Integer" else Float)(
                min_value=min_value,
                max_value=max_value,
                default_value=default_value)
        elif type_name == "String":
            min_length = self._extract_optional_number_attrib(attrib, "minlength")
            # if minlength is not defined default value is 1
            if min_length is None:
                min_length = 1
            max_length = self._extract_optional_number_attrib(attrib, "maxlength")
            default_value = self._extract_attrib(attrib, "defvalue")
            param_type = String(min_length=min_length, max_length=max_length, default_value=default_value)
        else:
            if type_name.count('.') == 1:
                custom_type_name = type_name.replace(".", "_")
            else:
                custom_type_name = prefix + type_name

            if custom_type_name in self._types:
                param_type = self._types[custom_type_name]
                default_value = self._extract_attrib(attrib, "defvalue")
                if default_value is not None:
                    if default_value not in param_type.elements:
                        raise ParseError("Default value '{}' for parameter '{}' is not a member of {}"
                                         .format(default_value, name, type(param_type.__name__)))
                    default_value = param_type.elements[default_value]
            else:
                raise ParseError("Unknown type '{}'".format(type_name))
        if self._extract_optional_bool_attrib(attrib, "array", False):
            min_size = self._extract_optional_number_attrib(attrib, "minsize")
            max_size = self._extract_optional_number_attrib(attrib, "maxsize")
            param_type = Array(element_type=param_type,
                               min_size=min_size,
                               max_size=max_size)

        return param_type, default_value

    @staticmethod
    def _parse_base_enum_element(subelement, base_type, params):
        if not isinstance(base_type, (Enum, EnumSubset)):
            raise ParseError("Elements specified for parameter '{}' of type '{}'"
                             .format(params["name"], type(base_type).__name__))
        if isinstance(base_type, Enum):
            base_type = EnumSubset(
                name=params["name"],
                enum=base_type,
                description=params["description"],
                design_description=params["design_description"],
                issues=params["issues"],
                todos=params["todos"],
                allowed_elements={})
        if "name" not in subelement.attrib:
            raise ParseError("Element name is not specified for parameter '{}'".format(params["name"]))
        element_name = subelement.attrib["name"]
        if len(subelement.attrib) != 1:
            raise ParseError("Unexpected attributes for element '{}' of parameter '{}'"
                             .format(element_name, params["name"]))
        children = subelement.getchildren()
        for child in children:
            if child.tag == "description":
                children.remove(child)
        if len(children) != 0:
            raise ParseError("Unexpected subelements for element '{}' of parameter '{}'"
                             .format(element_name, params["name"]))
        if element_name in base_type.allowed_elements:
            raise ParseError("Element '{}' is specified more than once for parameter '{}'"
                             .format(element_name, params["name"]))
        if element_name not in base_type.enum.elements:
            raise ParseError("Element '{}' is not a member of enum '{}'".format(element_name, base_type.enum.name))
        base_type.allowed_elements[element_name] = base_type.enum.elements[element_name]
        return base_type

    def _extract_optional_bool_attrib(self, attrib, name, default):
        """Extract boolean attribute with given name.

        :param attrib: dict with attributes
        :param name: string with attribute name (array)
        :param default: bool
        :return: value of the attribute.
        """
        value = self._extract_attrib(attrib, name)

        if value is None:
            value = default
        else:
            value = self._get_bool_from_string(value)

        return value

    def _extract_optional_number_attrib(self, attrib, name, _type=int):
        """Extract number attribute with given name.

        :param attrib: dict with attributes
        :param name: string with attribute name
        :param _type: int
        :return: value of the attribute.
        """
        value = self._extract_attrib(attrib, name)

        if value is not None:
            try:
                value = _type(value)
            except:
                raise ParseError("Inlaid value for {} : '{}'".format(_type.__name__, value))

        return value

    @staticmethod
    def _extract_attrib(attrib, name):
        """Extract attribute with given name.

        :param attrib: dict with attributes
        :param name: string with attribute name
        :return: value of the attribute.
        """
        value = None

        if name in attrib:
            value = attrib[name]
            del attrib[name]

        return value

    @staticmethod
    def _get_bool_from_string(bool_string):
        """Convert string representation of boolean to real bool value.

        :param bool_string: string with attribute value
        :return: converted value.
        """

        if bool_string in ['0', 'false']:
            value = False
        elif bool_string in ['1', 'true']:
            value = True
        else:
            raise ParseError("Invalid value for bool: '{}'".format(bool_string))

        return value

    @staticmethod
    def _ignore_attribute(attrib, name):
        """To be called when attribute is meaningless in terms
        of code generation but it's presence is not issue.

        Removes this attribute from attribute list.

        :param attrib: dict with attributes
        :param name: string with attribute name
        :return: True if name in attrib
        """
        if name in attrib:
            del attrib[name]
        return True

    @staticmethod
    def _parse_version(version):
        """Validates if a version supplied is in the correct
           format of Major.Minor.Patch. If Major.Minor format
           is supplied, a patch version of 0 will be added to
           the end.

        :param version: string with attribute value
        :return: string with validated version
        """

        pattern = re.compile(r'(\d+\.\d+\.\d+|\d+\.\d+)')
        result = pattern.match(version)
        if result is None or (result.end() != len(version)):
            raise ParseError("Incorrect format of version please check MOBILE_API.xml. "
                             "Need format of major_version.minor_version or major_version.minor_version.patch_version")

        version_array = version.split(".")
        if len(version_array) == 2:
            version_array.append("0")
        dot_str = "."
        return dot_str.join(version_array)

    def _parse_history(self, history, prefix, parent):
        """Searching for element parent

        :param history: an instance of Element (from ElementTree)
        :param prefix: empty string
        :param parent: an instance of Element (from ElementTree)
        :return: list with items where subelement.tag == parent.tag
        """
        if history.tag != "history":
            raise ParseError("Invalid history tag: " + history.tag)

        items = []

        for subelement in history:
            if subelement.tag == "enum" and parent.tag == "enum":
                items.append(self._parse_enum(subelement, prefix))
            elif subelement.tag == "element" and parent.tag == "element":
                items.append(self._parse_enum_element(subelement))
            elif subelement.tag == "description" and parent.tag == "description":
                items.append(self._parse_simple_element(subelement))
            elif subelement.tag == "struct" and parent.tag == "struct":
                items.append(self._parse_struct(subelement, prefix))
            elif subelement.tag == "param" and parent.tag == "param":
                items.append(self._parse_function_param(subelement, prefix))
            elif subelement.tag == "function" and parent.tag == "function":
                items.append(self._parse_function(subelement, prefix))
            else:
                raise ParseError("A history tag must be nested within the element it notes "
                                 "the history for. Fix item: '{}'".format(parent.attrib["name"]))

        return items
