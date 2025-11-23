import unittest
import timeout_decorator
import ansible.utils.color as module_0

class Test_Color_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'blue'
            var_0 = module_0.parsecolor(str_0)
            str_1 = 'color123'
            var_1 = module_0.parsecolor(str_1)
            str_2 = 'rgb123'
            var_2 = module_0.parsecolor(str_2)
            str_3 = 'gray5'
            var_3 = module_0.parsecolor(str_3)
            str_4 = 'pink'
            var_4 = module_0.parsecolor(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
