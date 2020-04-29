"""Issue.

"""


class Issue:
    """Issue.

    Issue must not contain subelements and attributes.
    @see RPCBase._parse_issue(element)

    :param creator: element.attrib["creator"]
    :param value: element.text

    """

    def __init__(self, creator=None, value=None):
        self.creator = creator
        self.value = value
