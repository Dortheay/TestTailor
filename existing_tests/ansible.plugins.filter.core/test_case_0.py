import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = {}
            list_0 = [dict_0, dict_0, dict_0]
            var_0 = module_0.to_nice_yaml(dict_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
