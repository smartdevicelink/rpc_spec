"""String type.

"""


class String:
    """String type.

    :param min_length: minimum string length
    :param max_length: maximum string length
    :param default_value: default value

    """

    def __init__(self, min_length=None, max_length=None, default_value=None):
        self.min_length = min_length
        self.max_length = max_length
        self.default_value = default_value
