import unittest
import timeout_decorator
import ansible.modules.subversion as module_0

class Test_Subversion_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            bytes_0 = b'\xf4\xde\xf6l\xf6\xfb\xe4:\xdcgO\xcau'
            set_0 = {bytes_0}
            int_0 = -4552
            float_0 = None
            str_0 = None
            str_1 = '6U~b'
            int_1 = 69
            bytes_1 = b'2\x94`\x8c\xe0\xbf\x0e\xdd\xcc'
            subversion_0 = module_0.Subversion(int_0, float_0, str_0, str_1, int_1, str_1, bytes_1, set_0)
            list_0 = [set_0, subversion_0]
            bool_0 = True
            subversion_1 = module_0.Subversion(bytes_0, set_0, list_0, bool_0, subversion_0, set_0, list_0, bool_0)
            list_1 = [subversion_1, float_0, str_0, bytes_1]
            float_1 = 1928.0
            subversion_2 = module_0.Subversion(list_1, subversion_1, str_0, list_1, list_1, set_0, list_0, float_1)
            var_0 = subversion_2.needs_update()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
