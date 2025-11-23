import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_28(self):
        try:
            bool_0 = False
            array_0 = module_0.Array(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
