import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_79(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_78(self):
        try:
            object_0 = module_0.Object()
            bool_0 = True
            dict_0 = {bool_0: bool_0}
            any_0 = object_0.validate(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
