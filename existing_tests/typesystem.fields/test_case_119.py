import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_120(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_34(self):
        object_0 = module_0.Object()
        dict_0 = {}
        any_0 = object_0.validate(dict_0)

if __name__ == "__main__":
    unittest.main()
