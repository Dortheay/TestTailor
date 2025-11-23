import unittest
import timeout_decorator
import mimesis.schema as module_0

class Test_Schema_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'en'
            abstract_field_0 = module_0.AbstractField(str_0)
            str_1 = 'full_name'
            str_2 = "Expected 'full_name' to return a string."
            callable_0 = None
            dict_0 = {str_1: str_0, str_1: abstract_field_0, str_1: str_2}
            any_0 = abstract_field_0.__call__(str_1, callable_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
