import unittest
import timeout_decorator
import ansible.modules.debconf as module_0

class Test_Debconf_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = None
            float_0 = 2631.08
            bytes_0 = b'V=J\xd2'
            bytes_1 = None
            dict_0 = {}
            var_0 = module_0.set_selection(bool_0, float_0, bool_0, bytes_0, bytes_1, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
