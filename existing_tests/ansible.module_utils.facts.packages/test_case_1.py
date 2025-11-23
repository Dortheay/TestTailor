import unittest
import timeout_decorator
import ansible.module_utils.facts.packages as module_0

class Test_Packages_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.get_all_pkg_managers()

if __name__ == "__main__":
    unittest.main()
