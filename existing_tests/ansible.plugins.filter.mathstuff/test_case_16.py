import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            filter_module_0 = None
            bool_0 = True
            var_0 = module_1.max(filter_module_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
