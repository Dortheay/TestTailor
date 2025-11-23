import unittest
import timeout_decorator
import ansible.utils.helpers as module_0

class Test_Helpers_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = ' -i localhost, '
            float_0 = 1101.18
            tuple_0 = (float_0,)
            var_0 = module_0.deduplicate_list(tuple_0)
            str_1 = None
            float_1 = 2061.383
            list_0 = [str_1, str_0, float_1]
            var_1 = module_0.object_to_dict(float_1, list_0)
            bool_0 = None
            var_2 = module_0.pct_to_int(float_1, bool_0, str_1)
            int_0 = -542
            var_3 = module_0.deduplicate_list(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
