import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            int_0 = -178
            list_0 = [int_0]
            var_0 = module_1.human_readable(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
