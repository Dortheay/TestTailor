import unittest
import timeout_decorator
import ansible.utils.color as module_0

class Test_Color_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'red'
            var_0 = module_0.parsecolor(str_0)
            str_1 = 'blue'
            var_1 = module_0.parsecolor(str_1)
            str_2 = 'color123'
            var_2 = module_0.parsecolor(str_2)
            str_3 = 'rgb123'
            var_3 = module_0.parsecolor(str_3)
            str_4 = 'pink'
            var_4 = module_0.parsecolor(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
