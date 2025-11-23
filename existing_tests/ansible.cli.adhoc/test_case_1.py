import unittest
import timeout_decorator
import ansible.cli.adhoc as module_0

class Test_Adhoc_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            ad_hoc_c_l_i_0 = module_0.AdHocCLI()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
