import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'G9pu>\nXc5cX2nM}'
            var_0 = module_0.parse_kv(str_0)
            str_1 = "cC['C~bVl y<&WY`$"
            var_1 = module_0.split_args(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
