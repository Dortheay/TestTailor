import unittest
import timeout_decorator
import ansible.playbook.included_file as module_0

class Test_Included_file_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            dict_0 = {}
            bool_0 = True
            set_0 = None
            bool_1 = True
            str_0 = '18^R3?c]&~xK'
            tuple_0 = ()
            included_file_0 = module_0.IncludedFile(set_0, bool_1, str_0, tuple_0)
            list_0 = []
            int_0 = 2486
            set_1 = {int_0, bool_0}
            included_file_1 = module_0.IncludedFile(dict_0, list_0, str_0, set_1)
            var_0 = included_file_1.__eq__(included_file_0)
            bytes_0 = b'_\xdc'
            float_0 = 4359.578
            list_1 = [dict_0, float_0, str_0]
            included_file_2 = module_0.IncludedFile(str_0, bytes_0, float_0, list_1)
            var_1 = included_file_2.__eq__(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
