"""SDLRPCV2 parser.

Contains parser for SDLRPCV2 XML format.

"""

from collections import OrderedDict

from model.enum import Enum
from parsers.parse_error import ParseError
from parsers.rpc_base import RPCBase


class Parser(RPCBase):
    """SDLRPCV2 parser."""

    @property
    def get_version(self):
        return '1.0.0'

    @staticmethod
    def _initialize_enums():
        """Initialize enums.

        This implementation returns empty OrderedDict because in SDLRPCV2
        all enums must be declared explicitly in the XML file.

        """
        return OrderedDict()

    def _check_enum_name(self, enum):
        """Check enum name.

        This method is called to check whether the newly parsed enum's name
        conflicts with some predefined enum.
        As SDLRPCV2 has no predefined enums this implementation does nothing.

        :param enum: an instance of model.Enum
        """

    def _parse_function_id_type(self, function_name, attrib):
        """Parse function id and message type according to XML format.

        This implementation extracts attribute "FunctionID" as function id
        and messagetype as message type and searches them in enums
        "FunctionID" and "messageType". If at least one of them (or the entire
        enum) is missing it raises an error.

        :param function_name: string with function name
        :param attrib: dict with function attributes
        :return: function id and message type as an instances of EnumElement.
        """
        if "functionID" not in attrib:
            raise ParseError("No functionID specified for function '{}'".format(function_name))

        if "messagetype" not in attrib:
            raise ParseError("No messagetype specified for function '{}'".format(function_name))

        function_id = self._get_enum_element_for_function(
            "FunctionID",
            self._extract_attrib(attrib, "functionID"))
        message_type = self._get_enum_element_for_function(
            "messageType",
            self._extract_attrib(attrib, "messagetype"))

        return function_id, message_type

    def _get_enum_element_for_function(self, enum_name, element_name):
        """Get enum element with given name from given enumeration.

        :param enum_name: string "FunctionID" or "messageType"
        :param element_name: string with enum name value
        :return: an instance of generator.Model.EnumElement.
        """
        if enum_name not in self._types:
            raise ParseError("Enumeration '{}' must be declared before any function"
                             .format(enum_name))

        enum = self._types[enum_name]

        if not isinstance(enum, Enum):
            raise ParseError("'{}' is not an enumeration".format(enum_name))

        if element_name not in enum.elements:
            raise ParseError("'{}' is not a member of enum '{}'".format(element_name, enum_name))

        return enum.elements[element_name]