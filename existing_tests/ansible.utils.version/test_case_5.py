import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '"qP"Y~'
            alpha_0 = module_0._Alpha(str_0)
            float_0 = 692.8
            var_0 = alpha_0.__le__(alpha_0)
            alpha_1 = module_0._Alpha(float_0)
            var_1 = alpha_1.__gt__(alpha_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
