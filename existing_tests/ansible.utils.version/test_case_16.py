import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            bool_0 = False
            int_0 = -1704
            numeric_0 = module_0._Numeric(int_0)
            var_0 = numeric_0.__eq__(bool_0)
            str_0 = 'sJ\n*4A?N`'
            var_1 = numeric_0.__ge__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
