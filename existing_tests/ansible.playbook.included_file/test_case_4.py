import unittest
import timeout_decorator
import ansible.playbook.included_file as module_0

class Test_Included_file_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'E#Pmc"X_6G3'
            set_0 = {str_0, str_0}
            dict_0 = {}
            bool_0 = True
            int_0 = 993
            bool_1 = True
            float_0 = -222.0
            str_1 = 'https://galaxy.ansible.com/api/'
            included_file_0 = module_0.IncludedFile(int_0, bool_1, int_0, float_0, str_1)
            var_0 = included_file_0.process_include_results(set_0, dict_0, str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
