"""Element of enumeration.

"""

from model.interface_item_base import InterfaceItemBase


class EnumElement(InterfaceItemBase):
    """Element of enumeration.

    :param name: item name
    :param description: list of string description elements
    :param design_description: list of string design description elements
    :param issues: list of issues
    :param todos: list of string todo elements
    :param platform: optional platform (string or None)
    :param since: string that defines the rpc spec version an element was introduced
    :param until: string that defines the rpc spec version an element was removed, deprecated, or changed
    :param deprecated: boolean that defines if an element is planned to be removed in a future release
    :param removed: boolean that defines if an element was removed from the api
    :param history: array of api element signature changes

    :param internal_name: internal name of an element must be used by a
                          generator if it is provided (not None)
    :param value: optional element value
    :param hex_value: optional element hex value

    """

    def __init__(self, name, description=None, design_description=None,
                 issues=None, todos=None, platform=None, internal_name=None,
                 value=None, hex_value=None, since=None, until=None,
                 deprecated=None, removed=None, history=None):
        super(EnumElement, self).__init__(
            name, description=description, design_description=design_description,
            issues=issues, todos=todos, platform=platform, since=since,
            until=until, deprecated=deprecated, removed=removed, history=history)

        self.internal_name = internal_name
        self.value = value
        self.hex_value = hex_value

    @property
    def primary_name(self):
        """Primary name of the EnumElement.

        Return the 'internal_name' property if presented or 'name' property
        otherwise.

        """
        return self.name if self.internal_name is None else self.internal_name
