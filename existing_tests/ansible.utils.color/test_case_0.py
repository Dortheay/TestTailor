import unittest
import timeout_decorator
import ansible.utils.color as module_0

class Test_Color_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 443
            var_0 = module_0.parsecolor(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
