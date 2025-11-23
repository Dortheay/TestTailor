import unittest
import timeout_decorator
import ansible.utils.color as module_0

class Test_Color_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'b3Nc;4Hp'
            var_0 = module_0.parsecolor(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
