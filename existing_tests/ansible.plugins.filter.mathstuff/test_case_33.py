import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_25(self):
        try:
            set_0 = set()
            bool_0 = False
            var_0 = module_1.inversepower(set_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
