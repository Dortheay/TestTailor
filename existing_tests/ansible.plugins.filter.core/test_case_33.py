import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_33(self):
        try:
            float_0 = 13.739070690504445
            str_0 = '%vm|A|@'
            dict_0 = {str_0: float_0, float_0: float_0}
            dict_1 = {str_0: dict_0, str_0: dict_0, str_0: float_0}
            var_0 = module_0.to_yaml(dict_0, **dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
