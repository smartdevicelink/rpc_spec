"""Enumeration subset.

"""

from model.interface_item_base import InterfaceItemBase


class EnumSubset(InterfaceItemBase):
    """Enumeration subset.

    :param name: item name
    :param description: list of string description elements
    :param design_description: list of string design description elements
    :param issues: list of issues
    :param todos: list of string todo elements
    :param platform: optional platform (string or None)
    :param since:
    :param until:
    :param deprecated:
    :param removed:
    :param history:

    :param enum: enumeration
    :param allowed_elements: dictionary of elements of enumeration
                             which are allowed in this subset

    """

    def __init__(self, name, enum, description=None, design_description=None,
                 issues=None, todos=None, platform=None, allowed_elements=None,
                 since=None, until=None, deprecated=None, removed=None, history=None):
        super(EnumSubset, self).__init__(
            name, description=description, design_description=design_description,
            issues=issues, todos=todos, platform=platform,
            since=since, until=until, deprecated=deprecated, removed=removed, history=history)

        self.enum = enum
        self.allowed_elements = allowed_elements if allowed_elements is not None else {}
