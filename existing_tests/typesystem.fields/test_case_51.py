import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_52(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_51(self):
        try:
            int_0 = 1126
            tuple_0 = ()
            object_0 = module_0.Object(min_properties=int_0, required=tuple_0)
            any_0 = object_0.validate(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
