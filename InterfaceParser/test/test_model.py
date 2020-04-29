
"""Interface model unit test"""
import sys
import unittest
from pathlib import Path

sys.path.append(Path(__file__).absolute().parents[1].as_posix())

try:
    from model.enum_element import EnumElement
except ModuleNotFoundError as e:
    print(e)


class TestInterfaceModel(unittest.TestCase):
    """Test for interface model."""

    def test_enum_element_primary_name(self):
        """Test property primary_name of EnumElement."""
        element = EnumElement(name="name1")
        self.assertEqual("name1", element.primary_name)

        element = EnumElement(name="name2",
                              internal_name="internal_name1")
        self.assertEqual("internal_name1", element.primary_name)

        element.internal_name = None
        self.assertEqual("name2", element.primary_name)

        element.internal_name = "internal_name2"
        self.assertEqual("internal_name2", element.primary_name)


if __name__ == "__main__":
    unittest.main()
