import unittest
import timeout_decorator
import ansible.plugins.filter.mathstuff as module_0

class Test_Mathstuff_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'I6zJcVw\\W'
        str_1 = ']r4g\x0bT8H]'
        var_0 = module_0.difference(str_0, str_0, str_1)

if __name__ == "__main__":
    unittest.main()
