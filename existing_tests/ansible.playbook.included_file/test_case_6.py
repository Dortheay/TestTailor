import unittest
import timeout_decorator
import ansible.playbook.included_file as module_0

class Test_Included_file_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'E#Pmc"X_6G3'
            set_0 = {str_0, str_0}
            dict_0 = {}
            int_0 = 8
            bool_0 = False
            included_file_0 = module_0.IncludedFile(dict_0, set_0, dict_0, bool_0)
            var_0 = included_file_0.process_include_results(dict_0, int_0, set_0, str_0)
            int_1 = 993
            float_0 = -222.0
            included_file_1 = module_0.IncludedFile(int_1, bool_0, int_1, float_0, str_0)
            var_1 = included_file_1.process_include_results(set_0, dict_0, str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
