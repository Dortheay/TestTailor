import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            complex_0 = None
            list_0 = [complex_0, complex_0]
            str_0 = '/[I1P;'
            var_0 = module_1.difference(complex_0, list_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
