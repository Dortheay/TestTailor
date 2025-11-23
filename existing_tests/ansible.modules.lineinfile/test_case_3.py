import unittest
import timeout_decorator
import ansible.modules.lineinfile as module_0

class Test_Lineinfile_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            tuple_0 = ()
            float_0 = 277.795
            bytes_0 = b'\x1c='
            str_0 = 'sAEs2saN`7V"<S;#'
            set_0 = {str_0}
            int_0 = -1586
            bool_0 = True
            var_0 = module_0.present(tuple_0, float_0, bytes_0, str_0, set_0, int_0, bool_0, tuple_0, bool_0, bytes_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
