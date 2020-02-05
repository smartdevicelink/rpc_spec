"""Integer type.

"""


class Integer:
    """Integer type.
    :param min_value: minimum allowed value
    :param max_value: maximum allowed value
    :param default_value: default value
    """

    def __init__(self, min_value=None, max_value=None, default_value=None):
        self.min_value = min_value
        self.max_value = max_value
        self.default_value = default_value
