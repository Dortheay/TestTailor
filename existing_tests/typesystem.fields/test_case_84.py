import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_85(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_84(self):
        try:
            int_0 = 695
            number_0 = module_0.Number(multiple_of=int_0)
            any_0 = number_0.validate(int_0)
            int_1 = 4358
            any_1 = number_0.validate(int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
