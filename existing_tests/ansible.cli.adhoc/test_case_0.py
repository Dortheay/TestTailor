import unittest
import timeout_decorator
import ansible.cli.adhoc as module_0

class Test_Adhoc_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = '0Ie[(7Gx<\x0clP'
        ad_hoc_c_l_i_0 = module_0.AdHocCLI(str_0)
        var_0 = ad_hoc_c_l_i_0.run()
        bytes_0 = None
        ad_hoc_c_l_i_1 = module_0.AdHocCLI(bytes_0)

if __name__ == "__main__":
    unittest.main()
