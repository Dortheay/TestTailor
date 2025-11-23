import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_42(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_41(self):
        try:
            var_0 = module_0.combine()
            list_0 = None
            var_1 = module_0.get_hash(list_0)
            int_0 = 2784
            bool_0 = False
            bool_1 = True
            set_0 = {bool_0, int_0, bool_1, int_0}
            dict_0 = None
            var_2 = module_0.rand(bool_0, set_0, int_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
