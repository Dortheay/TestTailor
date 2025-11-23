import unittest
import timeout_decorator
import ansible.utils.helpers as module_0

class Test_Helpers_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'collection metadata must be an instance of Python Mapping'
            list_0 = None
            var_0 = module_0.pct_to_int(str_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
