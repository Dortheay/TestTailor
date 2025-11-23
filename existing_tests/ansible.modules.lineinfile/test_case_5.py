import unittest
import timeout_decorator
import ansible.modules.lineinfile as module_0

class Test_Lineinfile_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bytes_0 = b'2\x11|\x90M'
            bool_0 = False
            int_0 = -2186
            dict_0 = {}
            str_0 = ']|X&x,ZBWM'
            set_0 = {bool_0}
            var_0 = module_0.absent(bytes_0, bool_0, int_0, dict_0, str_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
