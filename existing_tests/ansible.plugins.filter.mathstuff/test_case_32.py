import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            bool_0 = False
            var_0 = module_1.logarithm(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
