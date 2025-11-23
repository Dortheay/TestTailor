import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_57(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_56(self):
        try:
            bool_0 = False
            field_0 = module_0.Field(default=bool_0)
            number_0 = module_0.Number(exclusive_minimum=field_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
