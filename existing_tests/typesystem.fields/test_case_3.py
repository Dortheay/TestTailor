import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            array_0 = module_0.Array()
            any_0 = array_0.validate(array_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
