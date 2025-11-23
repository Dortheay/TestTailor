import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_116(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_30(self):
        int_0 = -1235
        number_0 = module_0.Number(multiple_of=int_0)
        any_0 = number_0.validate(int_0)

if __name__ == "__main__":
    unittest.main()
