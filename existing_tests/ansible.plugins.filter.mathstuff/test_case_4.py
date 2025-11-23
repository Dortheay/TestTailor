import unittest
import timeout_decorator
import ansible.plugins.filter.mathstuff as module_0

class Test_Mathstuff_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        int_0 = 82
        list_0 = [int_0, int_0, int_0, int_0]
        var_0 = module_0.union(int_0, list_0, list_0)

if __name__ == "__main__":
    unittest.main()
