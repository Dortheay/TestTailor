import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_69(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_68(self):
        try:
            float_0 = None
            object_0 = module_0.Object()
            any_0 = object_0.validate(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
