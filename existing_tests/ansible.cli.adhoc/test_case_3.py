import unittest
import timeout_decorator
import ansible.cli.adhoc as module_0

class Test_Adhoc_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'ansible'
            str_1 = 'all'
            str_2 = '-m'
            str_3 = 'ping'
            str_4 = [str_0, str_1, str_2, str_3]
            ad_hoc_c_l_i_0 = module_0.AdHocCLI(str_4)
            var_0 = ad_hoc_c_l_i_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
