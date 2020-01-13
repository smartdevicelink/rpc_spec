"""SDLRPCV2 XML parser unit test."""
import sys
import unittest
from pathlib import Path

sys.path.append(Path(__file__).absolute().parents[2].as_posix())

try:
    from parsers.sdl_rpc_v2 import Parser
    from model.integer import Integer
    from model.boolean import Boolean
    from model.double import Double
    from model.array import Array
    from model.string import String
    from model.enum_subset import EnumSubset
except ModuleNotFoundError as error:
    print(error)


class TestSDLRPCV2Parser(unittest.TestCase):
    """Test for SDLRPCV2 xml parser."""

    class _Issue:
        def __init__(self, creator, value):
            self.creator = creator
            self.value = value

        def __eq__(self, other):
            return self.creator == other.creator and self.value == other.value

    def setUp(self):
        """Test initialization."""
        valid_xml_name = Path(__file__).parents[0].joinpath('valid_SDLRPCV2.xml').as_posix()
        self.interface = Parser().parse(valid_xml_name)
        self.assertIsNotNone(self.interface)

    def test_valid_xml(self):
        """Test parsing of valid xml."""

        self.assertEqual(2, len(self.interface.params))
        self.assertDictEqual({"attribute1": "value1", "attribute2": "value2"},
                             self.interface.params)
    def test_enumerations(self):
        """
        Enumerations
        """
        self.assertEqual(3, len(self.interface.enums))

    def test_enumeration_function_id(self):
        """
        Enumeration "FunctionID"
        """
        self.assertIn("FunctionID", self.interface.enums)
        enum = self.interface.enums["FunctionID"]
        self.verify_base_item(item=enum,
                              name="FunctionID",
                              description=["Description string 1",
                                           "Description string 2"],
                              todos=['Function id todo'])
        self.assertIsNone(enum.internal_scope)

        self.assertEqual(2, len(enum.elements))

        self.assertIn("Function1_id", enum.elements)
        element = enum.elements["Function1_id"]
        self.verify_base_item(
            item=element,
            name="Function1_id",
            design_description=["Function1 element design description"])
        self.assertIsNone(element.internal_name)
        self.assertEqual(10, element.value)

        self.assertIn("Function2_id", enum.elements)
        element = enum.elements["Function2_id"]
        self.verify_base_item(
            item=element,
            name="Function2_id")
        self.assertEqual("Function2_internal", element.internal_name)
        self.assertIsNone(element.value)

    def test_enumeration_message_type(self):
        """
        Enumeration "messageType"
        """
        self.assertIn("messageType", self.interface.enums)
        enum = self.interface.enums["messageType"]
        self.verify_base_item(
            item=enum,
            name="messageType",
            design_description=["messageType design description",
                                "messageType design description 2"],
            issues=[TestSDLRPCV2Parser._Issue(
                creator="messageType issue creator",
                value="Issue text")])
        self.assertIsNone(enum.internal_scope)

        self.assertEqual(3, len(enum.elements))

        self.assertIn("request", enum.elements)
        element = enum.elements["request"]
        self.verify_base_item(item=element,
                              name="request",
                              todos=["request todo 1", "request todo 2"],
                              issues=[TestSDLRPCV2Parser._Issue(
                                  creator="issue creator",
                                  value="request issue")])
        self.assertIsNone(element.internal_name)
        self.assertEqual(0, element.value)

        self.assertIn("response", enum.elements)
        element = enum.elements["response"]
        self.verify_base_item(item=element, name="response")
        self.assertIsNone(element.internal_name)
        self.assertEqual(1, element.value)

        self.assertIn("notification", enum.elements)
        element = enum.elements["notification"]
        self.verify_base_item(item=element, name="notification")
        self.assertIsNone(element.internal_name)
        self.assertEqual(2, element.value)

    def test_enumeration_enum1(self):
        """
        Enumeration "enum1"
        """
        self.assertIn("enum1", self.interface.enums)
        enum = self.interface.enums["enum1"]
        self.verify_base_item(item=enum, name="enum1",
                              platform="enum1 platform")
        self.assertEqual("scope", enum.internal_scope)

        self.assertEqual(3, len(enum.elements))

        self.assertIn("element1", enum.elements)
        element = enum.elements["element1"]
        self.verify_base_item(item=element, name="element1")
        self.assertIsNone(element.internal_name)
        self.assertEqual(10, element.value)

        self.assertIn("element2", enum.elements)
        element = enum.elements["element2"]
        self.verify_base_item(item=element, name="element2")
        self.assertEqual("element2_internal", element.internal_name)
        self.assertEqual(11, element.value)

        self.assertIn("element3", enum.elements)
        element = enum.elements["element3"]
        self.verify_base_item(
            item=element,
            name="element3",
            design_description=["Element design description"],
            platform="element3 platform")
        self.assertIsNone(element.internal_name)
        self.assertIsNone(element.value)

    def test_structures(self):
        """
        Structures
        """
        self.assertEqual(2, len(self.interface.structs))

    def test_structure_struct1(self):
        """
        Structure "struct1"
        """
        self.assertIn("struct1", self.interface.structs)
        struct = self.interface.structs["struct1"]
        self.verify_base_item(
            item=struct,
            name="struct1",
            description=["Struct description"],
            issues=[TestSDLRPCV2Parser._Issue(creator="creator1",
                                              value="Issue1"),
                    TestSDLRPCV2Parser._Issue(creator="creator2",
                                              value="Issue2")])

        self.assertEqual(4, len(struct.members))

        self.assertIn("member1", struct.members)
        member = struct.members["member1"]
        self.verify_base_item(
            item=member,
            name="member1",
            description=["Param1 description"])
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, Integer)
        self.assertIsNone(member.param_type.min_value)
        self.assertIsNone(member.param_type.max_value)

        self.assertIn("member2", struct.members)
        member = struct.members["member2"]
        self.verify_base_item(item=member, name="member2",
                              platform="member2 platform")
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, Boolean)

        self.assertIn("member3", struct.members)
        member = struct.members["member3"]
        self.verify_base_item(item=member, name="member3")
        self.assertEqual(False, member.is_mandatory)
        self.assertIsInstance(member.param_type, Double)
        self.assertIsNone(member.param_type.min_value)
        self.assertAlmostEqual(20.5, member.param_type.max_value)

        self.assertIn("member4", struct.members)
        member = struct.members["member4"]
        self.verify_base_item(item=member, name="member4")
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, Array)
        self.assertIsNone(member.param_type.min_size)
        self.assertIsNone(member.param_type.max_size)
        self.assertIsInstance(member.param_type.element_type, Integer)
        self.assertEqual(11, member.param_type.element_type.min_value)
        self.assertEqual(100, member.param_type.element_type.max_value)

    def test_structure_struct2(self):
        """
        Structure "struct2"
        """
        self.assertIn("struct2", self.interface.structs)
        struct = self.interface.structs["struct2"]
        self.verify_base_item(item=struct,
                              name="struct2",
                              description=["Description of struct2"],
                              platform="struct2 platform")

        self.assertEqual(4, len(struct.members))

        self.assertIn("m1", struct.members)
        member = struct.members["m1"]
        self.verify_base_item(item=member, name="m1")
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, String)
        self.assertIsNone(member.param_type.max_length)

        self.assertIn("m2", struct.members)
        member = struct.members["m2"]
        self.verify_base_item(item=member, name="m2")
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, Array)
        self.assertEqual(1, member.param_type.min_size)
        self.assertEqual(50, member.param_type.max_size)
        self.assertIsInstance(member.param_type.element_type, String)
        self.assertEqual(100, member.param_type.element_type.max_length)

        self.assertIn("m3", struct.members)
        member = struct.members["m3"]
        self.verify_base_item(item=member, name="m3")
        self.assertTrue(member.is_mandatory)
        self.assertIs(member.param_type, self.interface.enums["enum1"])

        self.assertIn("m4", struct.members)
        member = struct.members["m4"]
        self.verify_base_item(item=member, name="m4")
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, Array)
        self.assertIsNone(member.param_type.min_size)
        self.assertEqual(10, member.param_type.max_size)
        self.assertIs(member.param_type.element_type, self.interface.structs["struct1"])

    def test_functions(self):
        """
        Functions
        """
        self.assertEqual(3, len(self.interface.functions))

    def test_function_request_function1(self):
        """
        Function request "Function1"
        """
        self.assertIn(
            (self.interface.enums["FunctionID"].elements["Function1_id"],
             self.interface.enums["messageType"].elements["request"]),
            self.interface.functions)
        func = self.interface.functions[
            (self.interface.enums["FunctionID"].elements["Function1_id"],
             self.interface.enums["messageType"].elements["request"])]
        self.verify_base_item(
            item=func,
            name="Function1",
            description=["Description of request Function1"],
            todos=["Function1 request todo"])
        self.assertIs(func.function_id,
                      self.interface.enums["FunctionID"].elements["Function1_id"])
        self.assertIs(func.message_type,
                      self.interface.enums["messageType"].elements["request"])

        self.assertEqual(3, len(func.params))

        self.assertIn("param1", func.params)
        param = func.params["param1"]
        self.verify_base_item(
            item=param,
            name="param1",
            issues=[TestSDLRPCV2Parser._Issue(creator="", value="")])
        self.assertEqual(False, param.is_mandatory)
        self.assertIsInstance(param.param_type, String)
        self.assertIsNone(param.param_type.max_length)
        self.assertIsNone(param.default_value)
        self.assertEqual("String default value", param.param_type.default_value)

        self.assertIn("param2", func.params)
        param = func.params["param2"]
        self.verify_base_item(
            item=param,
            name="param2",
            description=["Param2 description", ""],
            todos=["Param2 todo"],
            platform="param2 platform")
        self.assertTrue(param.is_mandatory)
        self.assertIsInstance(param.param_type, Integer)
        self.assertIsNone(param.param_type.min_value)
        self.assertIsNone(param.param_type.max_value)
        self.assertIsNone(param.default_value)

        self.assertIn("param3", func.params)
        param = func.params["param3"]
        self.verify_base_item(item=param, name="param3")
        self.assertEqual(False, param.is_mandatory)
        self.assertIs(param.param_type, self.interface.structs["struct1"])
        self.assertIsNone(param.default_value)

    def test_function_response_function1(self):
        """
        Function response "Function1"
        """
        self.assertIn(
            (self.interface.enums["FunctionID"].elements["Function1_id"],
             self.interface.enums["messageType"].elements["response"]),
            self.interface.functions)
        func = self.interface.functions[
            (self.interface.enums["FunctionID"].elements["Function1_id"],
             self.interface.enums["messageType"].elements["response"])]
        self.verify_base_item(
            item=func,
            name="Function1",
            issues=[TestSDLRPCV2Parser._Issue(creator="c1", value=""),
                    TestSDLRPCV2Parser._Issue(creator="c2", value="")],
            platform="")
        self.assertIs(func.function_id,
                      self.interface.enums["FunctionID"].elements["Function1_id"])
        self.assertIs(func.message_type,
                      self.interface.enums["messageType"].elements["response"])

        self.assertEqual(3, len(func.params))

        self.assertIn("p1", func.params)
        param = func.params["p1"]
        self.verify_base_item(item=param, name="p1")
        self.assertTrue(param.is_mandatory)
        self.assertIs(param.param_type, self.interface.enums["enum1"])
        self.assertIsNone(param.default_value)

        self.assertIn("p2", func.params)
        param = func.params["p2"]
        self.verify_base_item(item=param, name="p2")
        self.assertTrue(param.is_mandatory)
        self.assertIs(param.param_type, self.interface.enums["enum1"])
        self.assertIsNone(param.default_value)
        self.assertIs(param.param_type.elements["element2"],
                      self.interface.enums["enum1"].elements["element2"])

        self.assertIn("p3", func.params)
        param = func.params["p3"]
        self.verify_base_item(item=param, name="p3", design_description=[""])
        self.assertTrue(param.is_mandatory)
        self.assertIsInstance(param.param_type, Boolean)
        self.assertIsNone(param.default_value)
        self.assertEqual(False, param.param_type.default_value)

    def test_function_notification_function2(self):
        """
        Function notification "Function2"
        """
        self.assertIn(
            (self.interface.enums["FunctionID"].elements["Function2_id"],
             self.interface.enums["messageType"].elements["notification"]),
            self.interface.functions)
        func = self.interface.functions[
            (self.interface.enums["FunctionID"].elements["Function2_id"],
             self.interface.enums["messageType"].elements["notification"])]
        self.verify_base_item(item=func,
                              name="Function2",
                              description=["Function2 description"],
                              platform="function2 platform")
        self.assertIs(func.function_id,
                      self.interface.enums["FunctionID"].elements["Function2_id"])
        self.assertIs(func.message_type,
                      self.interface.enums["messageType"].elements["notification"])

        self.assertEqual(3, len(func.params))

        self.assertIn("n1", func.params)
        param = func.params["n1"]
        self.verify_base_item(item=param, name="n1", todos=["n1 todo"])
        self.assertTrue(param.is_mandatory)
        self.assertIsInstance(param.param_type, EnumSubset)
        self.assertIs(param.param_type.enum, self.interface.enums["enum1"])
        self.assertDictEqual(
            {"element2": self.interface.enums["enum1"].elements["element2"],
             "element3": self.interface.enums["enum1"].elements["element3"]},
            param.param_type.allowed_elements)
        self.assertIsNone(param.default_value)

        self.assertIn("n2", func.params)
        param = func.params["n2"]
        self.verify_base_item(item=param, name="n2", todos=["n2 todo"])
        self.assertTrue(param.is_mandatory)
        self.assertIsInstance(param.param_type, Array)
        self.assertEqual(1, param.param_type.min_size)
        self.assertEqual(100, param.param_type.max_size)
        self.assertIsInstance(param.param_type.element_type, EnumSubset)
        self.assertIs(param.param_type.element_type.enum,
                      self.interface.enums["enum1"])
        self.assertDictEqual(
            {"element1": self.interface.enums["enum1"].elements["element1"],
             "element3": self.interface.enums["enum1"].elements["element3"]},
            param.param_type.element_type.allowed_elements)
        self.assertIsNone(param.default_value)

        self.assertIn("n3", func.params)
        param = func.params["n3"]
        self.verify_base_item(item=param, name="n3")
        self.assertEqual(False, param.is_mandatory)
        self.assertIs(param.param_type, self.interface.structs["struct2"])
        self.assertIsNone(param.default_value)

    def verify_base_item(self, item, name, description=None,
                         design_description=None, issues=None, todos=None,
                         platform=None):
        """Verify base self.interface item variables."""
        self.assertEqual(name, item.name)
        self.assertSequenceEqual(self.get_list(description), item.description)
        self.assertSequenceEqual(self.get_list(design_description),
                                 item.design_description)
        self.assertSequenceEqual(self.get_list(issues), item.issues)
        self.assertSequenceEqual(self.get_list(todos), item.todos)
        self.assertEqual(platform, item.platform)

    @staticmethod
    def get_list(l=None):
        """Return provided list or empty list if None is provided."""
        return l if l is not None else []


if __name__ == "__main__":
    unittest.main()
