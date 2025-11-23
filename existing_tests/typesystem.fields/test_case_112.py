import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_113(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        number_0 = module_0.Number()
        int_0 = -961
        any_0 = number_0.validate(int_0)

if __name__ == "__main__":
    unittest.main()
