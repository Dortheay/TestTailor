import unittest
import timeout_decorator
import ansible.modules.subversion as module_0

class Test_Subversion_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'H,2*'
            dict_0 = {str_0: str_0, str_0: str_0}
            str_1 = '\rC4HU?0*QL8@b8LP4)$'
            str_2 = '__main__'
            tuple_0 = (str_1, str_2)
            float_0 = 730.83
            int_0 = -44
            bytes_0 = b'\xf9\xe4n\xf2\x05z+S\x80\xbfV\\\x86;\xf8$\xf2'
            int_1 = 30
            dict_1 = {int_1: tuple_0, bytes_0: float_0}
            list_0 = [str_1]
            set_0 = set()
            str_3 = '&U!|A8e)H7A5U.:[ECP'
            str_4 = '^iZE8FR\x0b7r&pt{\r\x0bSv'
            bytes_1 = b"\xfc\xe9\xb2\xc6,(\xf3x\x0e\x90\x9e'\x06Va\x0f\x9eyy>"
            int_2 = None
            bytes_2 = b'\xd3\xb4\xe9_5\x9cK\xc5\xa6 @?\xca\xab'
            subversion_0 = module_0.Subversion(set_0, int_2, tuple_0, bytes_2, list_0, int_1, dict_0, set_0)
            float_1 = -848.0
            bytes_3 = b'\xfa\xdaT\xac\xfdlO0Lc\x9b\xf6xJ\n\xf8\x1ds'
            subversion_1 = module_0.Subversion(dict_0, subversion_0, float_1, dict_0, float_1, bytes_3, list_0, set_0)
            subversion_2 = module_0.Subversion(list_0, str_4, int_0, set_0, bytes_1, tuple_0, subversion_0, subversion_1)
            bytes_4 = b'K\xf7\x8f9\x10?\x91sof'
            float_2 = 1861.828684
            subversion_3 = module_0.Subversion(subversion_2, bytes_4, list_0, float_0, tuple_0, dict_1, float_2, set_0)
            str_5 = 'U+bo#4-OU*'
            dict_2 = {tuple_0: subversion_3, int_2: set_0, str_3: int_1, str_5: bytes_2}
            bool_0 = True
            subversion_4 = module_0.Subversion(dict_1, set_0, str_3, dict_2, dict_0, list_0, int_2, bool_0)
            subversion_5 = module_0.Subversion(int_1, bytes_0, dict_1, bytes_0, int_1, list_0, subversion_4, dict_0)
            var_0 = subversion_5.update()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
