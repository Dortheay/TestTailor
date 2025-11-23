import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '"qP"Y~'
            alpha_0 = module_0._Alpha(str_0)
            bool_0 = False
            var_0 = alpha_0.__ne__(bool_0)
            float_0 = 692.8
            var_1 = alpha_0.__le__(alpha_0)
            alpha_1 = module_0._Alpha(float_0)
            var_2 = alpha_1.__gt__(alpha_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
