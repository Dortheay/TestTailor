import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_30(self):
        try:
            str_0 = ''
            float_0 = -5.3582391175729365
            var_0 = module_0.from_yaml(float_0)
            dict_0 = {var_0: float_0}
            int_0 = None
            list_0 = []
            var_1 = module_0.extract(dict_0, int_0, str_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
