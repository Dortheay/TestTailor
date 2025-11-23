import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 2288
            display_0 = module_0.Display(int_0)
            var_0 = module_1.unique(display_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
