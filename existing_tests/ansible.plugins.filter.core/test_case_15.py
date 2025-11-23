import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            dict_0 = None
            list_0 = [dict_0]
            list_1 = []
            float_0 = -1161.1
            str_0 = 'wb'
            tuple_0 = (float_0, str_0)
            var_0 = module_0.do_groupby(list_0, list_1, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
