import unittest
import timeout_decorator
import ansible.module_utils.splitter as module_0

class Test_Splitter_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '"hello"'
        var_0 = module_0.is_quoted(str_0)
        str_1 = "'world'"
        var_1 = module_0.is_quoted(str_1)
        str_2 = '"mis"matched\''
        var_2 = module_0.is_quoted(str_2)
        str_3 = 'no_quotes'
        var_3 = module_0.is_quoted(str_3)
        str_4 = ''
        var_4 = module_0.is_quoted(str_4)

if __name__ == "__main__":
    unittest.main()
