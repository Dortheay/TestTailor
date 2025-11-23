import unittest
import timeout_decorator
import ansible.modules.subversion as module_0

class Test_Subversion_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            dict_0 = {}
            str_0 = ''
            bytes_0 = b'\xe2\x05~\xfa\r\x9dE\x92\xfb\xab\xe8\x89'
            float_0 = 2457.75
            tuple_0 = (bytes_0, float_0)
            list_0 = [tuple_0, str_0, bytes_0]
            int_0 = 90
            bool_0 = True
            float_1 = 429.2842
            bytes_1 = b'\xd6\xf6.r/\xc6\xc1\xd2\x83'
            str_1 = 'ansible.modules.subversion'
            bytes_2 = b'\xd8\xe7\x9b'
            subversion_0 = module_0.Subversion(float_1, float_1, int_0, dict_0, tuple_0, str_1, list_0, bytes_2)
            subversion_1 = module_0.Subversion(dict_0, dict_0, bool_0, float_1, bytes_1, int_0, subversion_0, dict_0)
            var_0 = subversion_1.is_svn_repo()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
