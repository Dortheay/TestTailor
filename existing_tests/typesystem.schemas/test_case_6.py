import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            schema_definitions_0 = module_0.SchemaDefinitions()
            schema_0 = module_0.Schema()
            iterator_0 = schema_0.__iter__()
            iterator_1 = schema_0.__iter__()
            str_0 = schema_0.__repr__()
            reference_0 = module_0.Reference(str_0)
            iterator_2 = schema_definitions_0.__iter__()
            str_1 = schema_0.__repr__()
            bool_0 = False
            schema_definitions_0.__setitem__(str_0, bool_0)
            field_0 = module_1.Field(title=str_0, allow_null=bool_0)
            module_0.set_definitions(field_0, schema_definitions_0)
            any_0 = reference_0.serialize(iterator_1)
            bool_1 = schema_0.__eq__(bool_0)
            optional_0 = None
            int_0 = schema_0.__len__()
            optional_1 = None
            reference_1 = module_0.Reference(str_1)
            str_2 = 'f_\rVzZ6'
            reference_2 = module_0.Reference(str_2)
            any_1 = reference_0.serialize(optional_0)
            any_2 = reference_2.validate(optional_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
