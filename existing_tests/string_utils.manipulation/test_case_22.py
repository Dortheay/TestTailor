import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            bytes_0 = b'\xec\xb0\xec\xcf\x12\x10\xf4\xa2\xc7:\x81\x1b\xa6(\xbc\xc6'
            var_0 = module_0.camel_case_to_snake(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
