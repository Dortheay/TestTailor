import unittest
import timeout_decorator
import ansible.modules.subversion as module_0

class Test_Subversion_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = 680
            bool_0 = False
            bytes_0 = None
            tuple_0 = (bytes_0, bytes_0)
            str_0 = '!^T$:S('
            dict_0 = {str_0: bytes_0, bytes_0: bool_0}
            str_1 = 'ansible.modules.subversion'
            bool_1 = True
            float_0 = -129.197
            float_1 = -13.4
            str_2 = ')'
            str_3 = '__main__'
            float_2 = 2781.1767
            subversion_0 = module_0.Subversion(bool_1, float_0, float_1, dict_0, str_2, str_3, float_2, tuple_0)
            int_1 = 921
            subversion_1 = module_0.Subversion(str_1, bool_0, subversion_0, subversion_0, tuple_0, subversion_0, int_0, int_1)
            var_0 = subversion_1.has_local_mods()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
