"""JSONRPC XML parser unit test."""
import sys
import unittest
from pathlib import Path

sys.path.append(Path(__file__).absolute().parents[2].as_posix())

try:
    from parsers.hmi_api_rpc import Parser
    from model.array import Array
    from model.boolean import Boolean
    from model.float import Float
    from model.enum_subset import EnumSubset
    from model.integer import Integer
    from model.string import String
except ModuleNotFoundError as error:
    print(error)


class TestJSONRPCVParser(unittest.TestCase):
    """Test for JSONRPC xml parser."""

    class _Issue:
        def __init__(self, creator, value):
            self.creator = creator
            self.value = value

        def __eq__(self, other):
            return self.creator == other.creator and self.value == other.value

    def setUp(self):
        """Test initialization."""
        valid_xml_name = Path(__file__).parents[0].joinpath('valid_JSONRPC.xml').as_posix()
        self.interface = Parser().parse(valid_xml_name)
        self.assertIsNotNone(self.interface)

    def test_valid_xml(self):
        """Test parsing of valid xml."""

        self.assertEqual(9, len(self.interface.params))
        self.assertDictEqual({"attr1": "v1",
                              "attr2": "v2",
                              "interface1_attribute1": "value1",
                              "interface1_attribute2": "value2",
                              "interface1_issues": "Issue1\nIssue2",
                              "interface1_design_description": "dd",
                              "interface2_attribute": "value",
                              "interface2_description":
                                  "Description of interface2",
                              "interface2_todos": "i2 todo"},
                             self.interface.params)

    def test_enumerations(self):
        """
        Enumerations
        """
        self.assertEqual(5, len(self.interface.enums))

    def test_enumeration_function_id(self):
        """
        Enumeration "FunctionID"
        """
        self.assertIn("FunctionID", self.interface.enums)
        enum = self.interface.enums["FunctionID"]
        self.verify_base_item(item=enum,
                              name="FunctionID")
        self.assertIsNone(enum.internal_scope)

        self.assertEqual(3, len(enum.elements))

        self.assertIn("interface1.Function1", enum.elements)
        element = enum.elements["interface1.Function1"]
        self.verify_base_item(
            item=element,
            name="interface1.Function1")
        self.assertEqual("interface1_Function1", element.internal_name)
        self.assertIsNone(element.value)

        self.assertIn("interface1.Function2", enum.elements)
        element = enum.elements["interface1.Function2"]
        self.verify_base_item(
            item=element,
            name="interface1.Function2")
        self.assertEqual("interface1_Function2", element.internal_name)
        self.assertIsNone(element.value)

        self.assertIn("interface2.Function1", enum.elements)
        element = enum.elements["interface2.Function1"]
        self.verify_base_item(
            item=element,
            name="interface2.Function1")
        self.assertEqual("interface2_Function1", element.internal_name)
        self.assertIsNone(element.value)

    def test_enumeration_message_type(self):
        """
        Enumeration "messageType"
        """

        self.assertIn("messageType", self.interface.enums)
        enum = self.interface.enums["messageType"]
        self.verify_base_item(
            item=enum,
            name="messageType")
        self.assertIsNone(enum.internal_scope)

        self.assertEqual(3, len(enum.elements))

        self.assertIn("request", enum.elements)
        element = enum.elements["request"]
        self.verify_base_item(item=element,
                              name="request")
        self.assertIsNone(element.internal_name)
        self.assertIsNone(element.value)

        self.assertIn("response", enum.elements)
        element = enum.elements["response"]
        self.verify_base_item(item=element, name="response")
        self.assertIsNone(element.internal_name)
        self.assertIsNone(element.value)

        self.assertIn("notification", enum.elements)
        element = enum.elements["notification"]
        self.verify_base_item(item=element, name="notification")
        self.assertIsNone(element.internal_name)
        self.assertIsNone(element.value)

    def test_enumeration_interface1_enum1(self):
        """
        Enumeration "interface1_enum1"
        """

        self.assertIn("interface1_enum1", self.interface.enums)
        enum = self.interface.enums["interface1_enum1"]
        self.verify_base_item(item=enum, name="interface1_enum1",
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

    def test_enumeration_interface2_enum1(self):
        """
        Enumeration "interface2_enum1"
        """

        self.assertIn("interface2_enum1", self.interface.enums)
        enum = self.interface.enums["interface2_enum1"]
        self.verify_base_item(item=enum, name="interface2_enum1",
                              description=["Interface2 enum1 description"])
        self.assertIsNone(enum.internal_scope)

        self.assertEqual(2, len(enum.elements))

        self.assertIn("e1", enum.elements)
        element = enum.elements["e1"]
        self.verify_base_item(item=element, name="e1")
        self.assertEqual("int_e1", element.internal_name)
        self.assertEqual(0, element.value)

        self.assertIn("e2", enum.elements)
        element = enum.elements["e2"]
        self.verify_base_item(item=element, name="e2")
        self.assertEqual("int_e2", element.internal_name)
        self.assertEqual(10, element.value)

    def test_enumeration_interface2_enum2(self):
        """
        Enumeration "interface2_enum2"
        """

        self.assertIn("interface2_enum2", self.interface.enums)
        enum = self.interface.enums["interface2_enum2"]
        self.verify_base_item(item=enum, name="interface2_enum2",
                              platform="e2 platform")
        self.assertEqual("e2 scope", enum.internal_scope)

        self.assertEqual(3, len(enum.elements))

        self.assertIn("element1", enum.elements)
        element = enum.elements["element1"]
        self.verify_base_item(item=element, name="element1")
        self.assertIsNone(element.internal_name)
        self.assertIsNone(element.value)

        self.assertIn("element2", enum.elements)
        element = enum.elements["element2"]
        self.verify_base_item(item=element, name="element2")
        self.assertIsNone(element.internal_name)
        self.assertIsNone(element.value)

        self.assertIn("element3", enum.elements)
        element = enum.elements["element3"]
        self.verify_base_item(item=element, name="element3")
        self.assertIsNone(element.internal_name)
        self.assertIsNone(element.value)

    def test_structures(self):
        """
         Structures
        """
        self.assertEqual(3, len(self.interface.structs))

    def test_structure_interface1_struct1(self):
        """
        Structure "interface1_struct1"
        """

        self.assertIn("interface1_struct1", self.interface.structs)
        struct = self.interface.structs["interface1_struct1"]
        self.verify_base_item(
            item=struct,
            name="interface1_struct1",
            description=["Struct description"],
            issues=[TestJSONRPCVParser._Issue(creator="creator1",
                                              value="Issue1"),
                    TestJSONRPCVParser._Issue(creator="creator2",
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
        self.assertIsInstance(member.param_type, Float)
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

    def test_structure_interface1_struct2(self):
        """
        Structure "interface1_struct2"
        """

        self.assertIn("interface1_struct2", self.interface.structs)
        struct = self.interface.structs["interface1_struct2"]
        self.verify_base_item(item=struct,
                              name="interface1_struct2",
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
        self.assertIs(member.param_type, self.interface.enums["interface1_enum1"])

        self.assertIn("m4", struct.members)
        member = struct.members["m4"]
        self.verify_base_item(item=member, name="m4")
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, Array)
        self.assertIsNone(member.param_type.min_size)
        self.assertEqual(10, member.param_type.max_size)
        self.assertIs(member.param_type.element_type,
                      self.interface.structs["interface1_struct1"])

    def test_structure_interface2_struct1(self):
        """
        Structure "interface2_struct1"
        """

        self.assertIn("interface2_struct1", self.interface.structs)
        struct = self.interface.structs["interface2_struct1"]
        self.verify_base_item(item=struct, name="interface2_struct1")

        self.assertEqual(3, len(struct.members))

        self.assertIn("m_1", struct.members)
        member = struct.members["m_1"]
        self.verify_base_item(item=member, name="m_1")
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, Array)
        self.assertEqual(1, member.param_type.min_size)
        self.assertEqual(10, member.param_type.max_size)
        self.assertIs(member.param_type.element_type,
                      self.interface.enums["interface2_enum1"])

        self.assertIn("m_2", struct.members)
        member = struct.members["m_2"]
        self.verify_base_item(item=member, name="m_2")
        self.assertTrue(member.is_mandatory)
        self.assertIs(member.param_type, self.interface.enums["interface2_enum2"])

        self.assertIn("m_3", struct.members)
        member = struct.members["m_3"]
        self.verify_base_item(item=member, name="m_3")
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, String)
        self.assertEqual(20, member.param_type.max_length)

    def test_functions(self):
        """
        Functions
        """

        self.assertEqual(5, len(self.interface.functions))

    def test_function_request_interface1_function1(self):
        """
        Function request "interface1_Function1"
        """

        self.assertIn(
            (self.interface.enums["FunctionID"].elements["interface1.Function1"],
             self.interface.enums["messageType"].elements["request"]),
            self.interface.functions)
        func = self.interface.functions[
            (self.interface.enums["FunctionID"].elements["interface1.Function1"],
             self.interface.enums["messageType"].elements["request"])]
        self.verify_base_item(
            item=func,
            name="interface1_Function1",
            description=["Description of request Function1"],
            todos=["Function1 request todo"])
        self.assertIs(
            func.function_id,
            self.interface.enums["FunctionID"].elements["interface1.Function1"])
        self.assertIs(func.message_type,
                      self.interface.enums["messageType"].elements["request"])

        self.assertEqual(3, len(func.params))

        self.assertIn("param1", func.params)
        param = func.params["param1"]
        self.verify_base_item(
            item=param,
            name="param1",
            issues=[TestJSONRPCVParser._Issue(creator="", value="")])
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
        self.assertIs(param.param_type,
                      self.interface.structs["interface1_struct1"])
        self.assertIsNone(param.default_value)

    def test_function_response_interface1_function1(self):
        """
        Function response "interface1_Function1"
        """

        self.assertIn(
            (self.interface.enums["FunctionID"].elements["interface1.Function1"],
             self.interface.enums["messageType"].elements["response"]),
            self.interface.functions)
        func = self.interface.functions[
            (self.interface.enums["FunctionID"].elements["interface1.Function1"],
             self.interface.enums["messageType"].elements["response"])]
        self.verify_base_item(
            item=func,
            name="interface1_Function1",
            issues=[TestJSONRPCVParser._Issue(creator="c1", value=""),
                    TestJSONRPCVParser._Issue(creator="c2", value="")],
            platform="")
        self.assertIs(
            func.function_id,
            self.interface.enums["FunctionID"].elements["interface1.Function1"])
        self.assertIs(func.message_type,
                      self.interface.enums["messageType"].elements["response"])

        self.assertEqual(3, len(func.params))

        self.assertIn("p1", func.params)
        param = func.params["p1"]
        self.verify_base_item(item=param, name="p1")
        self.assertTrue(param.is_mandatory)
        self.assertIs(param.param_type, self.interface.enums["interface1_enum1"])
        self.assertIsNone(param.default_value)

        self.assertIn("p2", func.params)
        param = func.params["p2"]
        self.verify_base_item(item=param, name="p2")
        self.assertTrue(param.is_mandatory)
        self.assertIs(param.param_type, self.interface.enums["interface1_enum1"])
        self.assertIsNone(param.default_value)
        self.assertIsNone(param.param_type.default_value)
        self.assertIs(param.param_type.elements["element2"],
                      self.interface.enums["interface1_enum1"].elements["element2"])

        self.assertIn("p3", func.params)
        param = func.params["p3"]
        self.verify_base_item(item=param, name="p3", design_description=[""])
        self.assertTrue(param.is_mandatory)
        self.assertIsInstance(param.param_type, Boolean)
        self.assertIsNone(param.default_value)
        self.assertFalse(param.param_type.default_value)

    def test_function_notification_interface1_function2(self):
        """
        Function notification "interface1_Function2"
        """

        self.assertIn(
            (self.interface.enums["FunctionID"].elements["interface1.Function2"],
             self.interface.enums["messageType"].elements["notification"]),
            self.interface.functions)
        func = self.interface.functions[
            (self.interface.enums["FunctionID"].elements["interface1.Function2"],
             self.interface.enums["messageType"].elements["notification"])]
        self.verify_base_item(item=func,
                              name="interface1_Function2",
                              description=["Function2 description"],
                              platform="function2 platform")
        self.assertIs(
            func.function_id,
            self.interface.enums["FunctionID"].elements["interface1.Function2"])
        self.assertIs(func.message_type,
                      self.interface.enums["messageType"].elements["notification"])

        self.assertEqual(3, len(func.params))

        self.assertIn("n1", func.params)
        param = func.params["n1"]
        self.verify_base_item(item=param, name="n1", todos=["n1 todo"])
        self.assertTrue(param.is_mandatory)
        self.assertIsInstance(param.param_type, EnumSubset)
        self.assertIs(param.param_type.enum, self.interface.enums["interface1_enum1"])
        self.assertDictEqual(
            {"element2":
                 self.interface.enums["interface1_enum1"].elements["element2"],
             "element3":
                 self.interface.enums["interface1_enum1"].elements["element3"]},
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
                      self.interface.enums["interface1_enum1"])
        self.assertDictEqual(
            {"element1":
                 self.interface.enums["interface1_enum1"].elements["element1"],
             "element3":
                 self.interface.enums["interface1_enum1"].elements["element3"]},
            param.param_type.element_type.allowed_elements)
        self.assertIsNone(param.default_value)

        self.assertIn("n3", func.params)
        param = func.params["n3"]
        self.verify_base_item(item=param, name="n3")
        self.assertEqual(False, param.is_mandatory)
        self.assertIs(param.param_type,
                      self.interface.structs["interface1_struct2"])
        self.assertIsNone(param.default_value)

    def test_function_request_interface2_function1(self):
        """
        Function request "interface2_Function1"
        """

        self.assertIn(
            (self.interface.enums["FunctionID"].elements["interface2.Function1"],
             self.interface.enums["messageType"].elements["request"]),
            self.interface.functions)
        func = self.interface.functions[
            (self.interface.enums["FunctionID"].elements["interface2.Function1"],
             self.interface.enums["messageType"].elements["request"])]
        self.verify_base_item(item=func, name="interface2_Function1")
        self.assertIs(
            func.function_id,
            self.interface.enums["FunctionID"].elements["interface2.Function1"])
        self.assertIs(func.message_type,
                      self.interface.enums["messageType"].elements["request"])

        self.assertEqual(2, len(func.params))

        self.assertIn("param1", func.params)
        param = func.params["param1"]
        self.verify_base_item(item=param, name="param1")
        self.assertEqual(False, param.is_mandatory)
        self.assertIs(param.param_type, self.interface.enums["interface2_enum1"])
        self.assertIsNone(param.default_value)

        self.assertIn("param2", func.params)
        param = func.params["param2"]
        self.verify_base_item(item=param, name="param2")
        self.assertTrue(param.is_mandatory)
        self.assertIsInstance(param.param_type, Array)
        self.assertEqual(5, param.param_type.min_size)
        self.assertEqual(25, param.param_type.max_size)
        self.assertIs(param.param_type.element_type,
                      self.interface.structs["interface2_struct1"])
        self.assertIsNone(param.default_value)

    def test_function_notification_interface2_function1(self):
        """
        Function notification "interface2_Function1"
        """

        self.assertIn(
            (self.interface.enums["FunctionID"].elements["interface2.Function1"],
             self.interface.enums["messageType"].elements["notification"]),
            self.interface.functions)
        func = self.interface.functions[
            (self.interface.enums["FunctionID"].elements["interface2.Function1"],
             self.interface.enums["messageType"].elements["notification"])]
        self.verify_base_item(
            item=func,
            name="interface2_Function1",
            issues=[
                TestJSONRPCVParser._Issue(creator="c", value="Issue text")],
            platform="platform")
        self.assertIs(
            func.function_id,
            self.interface.enums["FunctionID"].elements["interface2.Function1"])
        self.assertIs(func.message_type,
                      self.interface.enums["messageType"].elements["notification"])

        self.assertEqual(2, len(func.params))

        self.assertIn("param", func.params)
        param = func.params["param"]
        self.verify_base_item(item=param, name="param")
        self.assertTrue(param.is_mandatory)
        self.assertIsInstance(param.param_type, EnumSubset)
        self.assertIs(param.param_type.enum,
                      self.interface.enums["interface2_enum2"])
        self.assertDictEqual(
            {"element2":
                 self.interface.enums["interface2_enum2"].elements["element2"],
             "element3":
                 self.interface.enums["interface2_enum2"].elements["element3"]},
            param.param_type.allowed_elements)
        self.assertIsNone(param.default_value)

        self.assertIn("i1", func.params)
        param = func.params["i1"]
        self.verify_base_item(item=param, name="i1")
        self.assertTrue(param.is_mandatory)
        self.assertIs(param.param_type, self.interface.structs["interface1_struct2"])
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
