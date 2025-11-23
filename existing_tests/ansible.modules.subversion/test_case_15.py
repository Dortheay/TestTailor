import unittest
import timeout_decorator
import ansible.modules.subversion as module_0

class Test_Subversion_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            int_0 = -1705
            list_0 = [int_0]
            bytes_0 = b'\x0c\x1d\xd6\xf6\xd35\x9a\xba\xea'
            str_0 = 'Q_WG&C|Uy/Z-,Rk-( '
            tuple_0 = ()
            bool_0 = True
            str_1 = '>^|P,e^twSl5a)}.`\x0cA'
            str_2 = ''
            set_0 = {tuple_0}
            dict_0 = {bytes_0: str_0, int_0: list_0, bytes_0: int_0}
            str_3 = 'chmod is not implemented for Powershell'
            subversion_0 = module_0.Subversion(bool_0, str_1, tuple_0, str_2, set_0, bool_0, dict_0, str_3)
            var_0 = subversion_0.switch()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
