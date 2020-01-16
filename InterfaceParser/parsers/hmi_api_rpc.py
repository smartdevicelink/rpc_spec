"""JSON RPC parser.

Contains parser for JSON RPC XML format.

"""
from parsers.parse_error import ParseError
from parsers.rpc_base import RPCBase


class Parser(RPCBase):
    """JSON RPC parser."""

    def __init__(self):
        """Constructor."""
        super(Parser, self).__init__()
        self._interface_name = None

    @property
    def get_version(self):
        return '1.0.0'

    def _parse_root(self, root):
        """Parse root XML element.

        This implementation parses root as interfaces element with multiple
        interfaces in it.

        :param root: ElementTree root Element object
        """

        self._params = root.attrib
        self._interface_name = None

        for element in root:
            if element.tag != "interface":
                raise ParseError("Subelement '{}' is unexpected in interfaces".format(element.tag))

            if "name" not in element.attrib:
                raise ParseError("Name is not specified for interface")

            self._interface_name = element.attrib["name"]
            self._parse_interface(element, self._interface_name + "_")

    def _check_enum_name(self, enum):
        """ Check enum name.

        This method is called to check whether the newly parsed enum's name
        conflicts with some predefined enum.
        As JSON RPC parser has no predefined enums this implementation does nothing.

        :param enum: an instance of model.Enum
        """

    def _provide_enum_element_for_function(self, enum_name, element_name):
        """Provide enum element for functions.

        This implementation replaces the underscore separating interface and
        function name with dot and sets it as name of enum element leaving
        the name with underscore as internal_name. For enums other than
        FunctionID the base implementation is called.

        :param enum_name: string with enum name
        :param element_name: string with interface name + function name
        :return: an instance of model.EnumElement
        """

        name = element_name
        internal_name = None

        if enum_name == 'FunctionID':
            prefix_length = len(self._interface_name) + 1
            if element_name[:prefix_length] != self._interface_name + '_':
                raise ParseError("Unexpected prefix for function id '{}'".format(element_name))
            name = "{}.{}".format(self._interface_name, element_name[prefix_length:])
            internal_name = element_name

        element = super(Parser, self)._provide_enum_element_for_function(
            enum_name,
            name)

        if internal_name is not None:
            element.internal_name = internal_name

        return element

    def _check_function_param_name(self, function_param_name):
        """Check function param name.

        This method is called to check whether the newly parsed function
        parameter name conflicts with some predefined name.

        :param function_param_name: string with function name
        """

        if function_param_name in ['method', 'code']:
            # pylint: disable=C0301
            raise ParseError("'{}' is a predefined name and can't be used as a function parameter name"
                             .format(function_param_name))
