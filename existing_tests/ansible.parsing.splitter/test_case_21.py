import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = 'a=b c=d'
            var_0 = module_0.split_args(str_0)
            str_1 = 'a="value with spaces" c=d'
            var_1 = module_0.split_args(str_1)
            str_2 = 'a={{ foo }} b={% bar %}'
            var_2 = module_0.split_args(str_2)
            str_3 = 'a="unterminated string b=c'
            var_3 = module_0.split_args(str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
