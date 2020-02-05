"""Array type.

"""


class Array:
    """Array type.

    :param min_size: minimum array size
    :param max_size: maximum array size
    :param element_type: type of array element

    """

    def __init__(self, min_size=None, max_size=None, element_type=None):
        self.min_size = min_size
        self.max_size = max_size
        self.element_type = element_type
