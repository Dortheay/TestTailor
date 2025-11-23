import unittest
import timeout_decorator
import ansible.modules.subversion as module_0

class Test_Subversion_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = 'crypt_id'
            str_1 = 'ansible.modules.subversion'
            set_0 = set()
            str_2 = 'ansible.modules.subversion'
            str_3 = "+ugo)H3'wHS["
            bytes_0 = b'\xe0'
            str_4 = 'gWSeeiX7Z'
            str_5 = '_*rAPn$\r'
            tuple_0 = (str_5,)
            str_6 = 'RCx}/gR[a,g=*'
            str_7 = '("*,n\x0c#cRxp\n%K'
            bool_0 = True
            float_0 = -1774.0
            dict_0 = None
            bool_1 = False
            subversion_0 = module_0.Subversion(str_7, bool_0, float_0, dict_0, bool_1, str_0, bytes_0, bool_0)
            int_0 = 340
            list_0 = None
            subversion_1 = module_0.Subversion(str_6, bytes_0, subversion_0, subversion_0, tuple_0, bool_0, int_0, list_0)
            list_1 = [bytes_0, subversion_1, str_4]
            subversion_2 = module_0.Subversion(bytes_0, tuple_0, list_1, bool_0, bool_0, list_1, set_0, int_0)
            subversion_3 = module_0.Subversion(str_0, str_1, set_0, str_2, str_3, bytes_0, str_4, subversion_2)
            var_0 = subversion_3.get_remote_revision()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
