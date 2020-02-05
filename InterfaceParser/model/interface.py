"""Interface

"""

from collections import OrderedDict


class Interface:
    """Interface.

    :param enums: dictionary of enumerations
    :param structs: dictionary of structures
    :param functions: dictionary of functions
    :param params: dictionary of interface parameters (name, version, etc.)

    """

    def __init__(self, enums=None, structs=None, functions=None, params=None):
        self.enums = enums if enums is not None else OrderedDict()
        self.structs = structs if structs is not None else OrderedDict()
        self.functions = functions if functions is not None else OrderedDict()
        self.params = params if params is not None else {}
