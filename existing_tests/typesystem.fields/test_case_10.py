import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'B9VkY1?G:Y+K'
            decimal_0 = module_0.Decimal()
            any_0 = decimal_0.serialize(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
