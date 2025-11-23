import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_105(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        int_0 = -956
        number_0 = module_0.Number(maximum=int_0, multiple_of=int_0)

if __name__ == "__main__":
    unittest.main()
