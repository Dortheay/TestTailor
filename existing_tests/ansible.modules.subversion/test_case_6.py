import unittest
import timeout_decorator
import ansible.modules.subversion as module_0

class Test_Subversion_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            float_0 = -327.483
            dict_0 = {float_0: float_0}
            set_0 = set()
            str_0 = 'eBML-g#e^3Y.Ccq>(OJ:'
            int_0 = 3636
            bytes_0 = b'\xd2q5\x83Y\xb7o\xb3\xb4\xaf\xfb\x00\xc9#\xdd\xf5\xcf"\x1c0'
            subversion_0 = module_0.Subversion(dict_0, float_0, str_0, int_0, str_0, bytes_0, set_0, str_0)
            var_0 = subversion_0.checkout(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
