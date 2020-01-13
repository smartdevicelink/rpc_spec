"""Base class for interface item.

"""

from abc import ABC


class InterfaceItemBase(ABC):
    """Base class for interface item.

    :param name: item name
    :param description: list of string description elements
    :param design_description: list of string design description elements
    :param issues: list of issues
    :param todos: list of string todo elements
    :param platform: optional platform (string or None)
    :param default_value: optional default value of this parameter
    :param scope: optional scope: internal, partner or none (none by defaul, means public)
    :param since:
    :param until:
    :param deprecated:
    :param removed:
    :param history:

    """

    def __init__(self, name, description=None, design_description=None,
                 issues=None, todos=None, platform=None, default_value=None, scope=None,
                 since=None, until=None, deprecated=None, removed=None, history=None):
        self.name = name
        self.description = description if description is not None else []
        self.design_description = design_description if design_description is not None else []
        self.issues = issues if issues is not None else []
        self.todos = todos if todos is not None else []
        self.platform = platform
        self.default_value = default_value
        self.scope = scope
        self.since = since
        self.until = until
        self.deprecated = deprecated
        self.removed = removed
        self.history = history
