import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = '#+f\x0bd(r@'
        str_1 = module_0.strip_margin(str_0)

if __name__ == "__main__":
    unittest.main()
