import unittest
import timeout_decorator
import ansible.playbook.included_file as module_0

class Test_Included_file_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = -156.31
            int_0 = 16
            set_0 = set()
            tuple_0 = (int_0, set_0)
            str_0 = '__omit_place_holder__%s'
            included_file_0 = module_0.IncludedFile(tuple_0, tuple_0, set_0, str_0)
            dict_0 = {}
            float_1 = 1656.43728
            included_file_1 = module_0.IncludedFile(included_file_0, dict_0, float_1, int_0)
            var_0 = included_file_1.__eq__(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
