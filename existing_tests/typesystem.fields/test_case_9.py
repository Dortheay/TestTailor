import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = ''
            number_0 = module_0.Number()
            any_0 = number_0.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
