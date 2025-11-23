import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = 'a=b c="foo bar" d=e'
            var_0 = module_0.split_args(str_0)
            str_1 = '{{ foo }} {{ bar }} a=b'
            var_1 = module_0.split_args(str_1)
            str_2 = 'a="This is a \\"quoted\\" string" b=c'
            var_2 = module_0.split_args(str_2)
            str_3 = 'a=b \\\nc=d'
            var_3 = module_0.split_args(str_3)
            str_4 = '{{ foo {{ bar }} }} a=b'
            var_4 = module_0.split_args(str_4)
            str_5 = 'a="unbalanced string'
            var_5 = module_0.split_args(str_5)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
