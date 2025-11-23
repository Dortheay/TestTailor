import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            str_0 = 'a=b c="foo bar"'
            var_0 = module_0.split_args(str_0)
            str_1 = 'a={{ x }} b="{% if y %}foo{% endif %}"'
            var_1 = module_0.split_args(str_1)
            str_2 = 'a="escaped \\"quotes\\"" b="{# comment #}"'
            var_2 = module_0.split_args(str_2)
            str_3 = 'a="unbalanced quote'
            var_3 = module_0.split_args(str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
