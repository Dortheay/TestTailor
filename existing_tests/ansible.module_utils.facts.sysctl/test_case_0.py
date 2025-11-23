import unittest
import timeout_decorator
import ansible.module_utils.facts.sysctl as module_0

class Test_Sysctl_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            list_0 = None
            var_0 = module_0.get_sysctl(list_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
