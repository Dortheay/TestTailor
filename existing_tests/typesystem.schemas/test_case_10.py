import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            schema_definitions_0 = module_0.SchemaDefinitions()
            iterator_0 = schema_definitions_0.__iter__()
            str_0 = '\n    Parse and validate a JSON string, rwturning positionally marked error\n    messages on parse or validation failures.\n\n    content - A JSON string or bytestring.\n    validator - A Field instance orSchema class to validate against.\n\n    Returns a two-tuple of (value, error_messages)\n    '
            optional_0 = None
            reference_0 = module_0.Reference(str_0)
            bool_0 = False
            any_0 = reference_0.validate(optional_0, strict=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
