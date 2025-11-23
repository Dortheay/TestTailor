import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_40(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_39(self):
        try:
            bytes_0 = b'\x1c\xd0'
            filter_module_0 = None
            dict_0 = {}
            var_0 = module_0.to_json(filter_module_0, **dict_0)
            int_0 = None
            var_1 = module_0.to_bool(int_0)
            bool_0 = False
            set_0 = {bytes_0, bytes_0}
            var_2 = module_0.regex_search(bool_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
