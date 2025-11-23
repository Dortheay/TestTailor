import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            str_0 = 'UDQ</+yUM'
            dict_0 = {str_0: str_0}
            bool_0 = False
            var_0 = module_0.extract(dict_0, dict_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
