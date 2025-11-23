import unittest
import timeout_decorator
import ansible.modules.subversion as module_0

class Test_Subversion_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = -1705
            bool_0 = False
            list_0 = [int_0]
            bytes_0 = b'\x0c\x1d\xd6\xf6\xd35\x9a\xba\xea'
            set_0 = {int_0}
            str_0 = 'Q_WG&C|Uy/Z-,Rk-( '
            list_1 = [set_0, str_0, str_0, list_0]
            tuple_0 = ()
            subversion_0 = module_0.Subversion(list_0, bytes_0, set_0, set_0, str_0, list_1, tuple_0, list_0)
            var_0 = subversion_0.checkout(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
