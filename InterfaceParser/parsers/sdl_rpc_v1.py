"""SDLRPCV1 parser.

Contains parser for SDLRPCV1 XML format.

"""
from parsers.parse_error import ParseError
from parsers.rpc_base import RPCBase


class Parser(RPCBase):
    """SDLRPCV1 parser."""

    @property
    def get_version(self):
        return '1.0.0'

    def _check_enum_name(self, enum):
        """ Check enum name.

        This method is called to check whether the newly parsed enum's name
        conflicts with some predefined enum.

        This implementation raises an error if enum name is one of the
        predefined enums "FunctionID" or "messageType" which must not be
        declared explicitly in the XML.

        :param enum: Enum object
        """
        if enum.name in ["FunctionID", "messageType"]:
            raise ParseError("Enum '{}' is generated automatically in SDLRPCV1 the original"
                             " declared in xml file will be ignored".format(enum.name))
