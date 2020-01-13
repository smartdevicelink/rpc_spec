"""Function.

"""

from collections import OrderedDict

from model.interface_item_base import InterfaceItemBase


class Function(InterfaceItemBase):
    """Function.

    :param name: item name
    :param description: list of string description elements
    :param design_description: list of string design description elements
    :param issues: list of issues
    :param todos: list of string todo elements
    :param platform: optional platform (string or None)
    :param scope: optional scope: internal, partner or none (none by defaul, means public)
    :param since:
    :param until:
    :param deprecated:
    :param removed:
    :param history:

    :param function_id: function identifier (EnumElement from Enum "FunctionID")
    :param message_type: message type (EnumElement from Enum "messageType")
    :param params: dictionary of function parameters (instances of FunctionParam class)

    """

    def __init__(self, name, function_id, message_type, description=None,
                 design_description=None, issues=None, todos=None,
                 platform=None, params=None, scope=None, since=None, until=None, deprecated=None, removed=None,
                 history=None):
        super(Function, self).__init__(
            name, description=description, design_description=design_description,
            issues=issues, todos=todos, platform=platform, scope=scope,
            since=since, until=until, deprecated=deprecated, removed=removed, history=history)

        self.function_id = function_id
        self.message_type = message_type
        self.params = params if params is not None else OrderedDict()
