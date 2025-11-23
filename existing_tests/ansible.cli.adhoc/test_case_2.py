import unittest
import timeout_decorator
import ansible.cli.adhoc as module_0

class Test_Adhoc_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\xdf\x8b\x00\x0f\xe6x0\xad\xd9Bs\x07\xe1\xc8'
            ad_hoc_c_l_i_0 = module_0.AdHocCLI(bytes_0)
            var_0 = ad_hoc_c_l_i_0.init_parser()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
