import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            int_0 = 1581
            var_0 = module_0.b64encode(int_0)
            str_0 = 'QEr2F7\x0bYQ\x0bl7*J('
            float_0 = 2.0
            var_1 = module_0.from_yaml(float_0)
            list_0 = [var_1, var_1, str_0]
            var_2 = module_0.combine(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
