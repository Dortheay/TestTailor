import unittest
import timeout_decorator
import ansible.module_utils.facts.packages as module_0

class Test_Packages_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            c_l_i_mgr_0 = module_0.CLIMgr()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
