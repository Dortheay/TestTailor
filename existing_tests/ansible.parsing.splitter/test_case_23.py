import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            str_0 = 'a=b c=d'
            var_0 = module_0.split_args(str_0)
            str_1 = 'a="foo bar" c="baz qux"'
            var_1 = module_0.split_args(str_1)
            str_2 = 'a={{ foo }} b={{ bar }}'
            var_2 = module_0.split_args(str_2)
            str_3 = 'a={{ "foo bar" }} b="baz qux"'
            var_3 = module_0.split_args(str_3)
            str_4 = 'a=\\"escaped\\" b="normal"'
            var_4 = module_0.split_args(str_4)
            str_5 = 'a="foo bar b=baz'
            var_5 = module_0.split_args(str_5)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
