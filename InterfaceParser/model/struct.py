"""Structure.

"""

from collections import OrderedDict

from model.interface_item_base import InterfaceItemBase


class Struct(InterfaceItemBase):
    """Structure.

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

    :param members: dictionary of structure members (instances of Param class)

    """

    def __init__(self, name, description=None, design_description=None,
                 issues=None, todos=None, platform=None, members=None, scope=None,
                 since=None, until=None, deprecated=None, removed=None, history=None):
        super(Struct, self).__init__(
            name, description=description, design_description=design_description,
            issues=issues, todos=todos, platform=platform, scope=scope,
            since=since, until=until, deprecated=deprecated, removed=removed, history=history)

        self.members = members if members is not None else OrderedDict()
