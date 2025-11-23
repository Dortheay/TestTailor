import unittest
import timeout_decorator
import ansible.modules.lineinfile as module_0

class Test_Lineinfile_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'fs'
            dict_0 = {}
            str_1 = '[=#okBV=U'
            bool_0 = True
            int_0 = 3234
            float_0 = 795.33618
            bytes_0 = b'>\xfd\x0e\x83\xc4\xc7\x1d\xbfj\x89\x8e\x0c\xcb\xcdk~x\xa8'
            var_0 = module_0.present(str_0, dict_0, str_0, str_1, str_1, bool_0, float_0, int_0, float_0, bytes_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
