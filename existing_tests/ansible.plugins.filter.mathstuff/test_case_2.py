import unittest
import timeout_decorator
import ansible.plugins.filter.mathstuff as module_0

class Test_Mathstuff_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = 743
        list_0 = []
        var_0 = module_0.unique(int_0, list_0)

if __name__ == "__main__":
    unittest.main()
