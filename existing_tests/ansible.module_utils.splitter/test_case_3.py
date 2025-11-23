import unittest
import timeout_decorator
import ansible.module_utils.splitter as module_0

class Test_Splitter_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = "'word'"
        var_0 = module_0.is_quoted(str_0)
        str_1 = '"mis"matched\''
        var_1 = module_0.is_quoted(str_1)
        str_2 = 'no_quotes'
        var_2 = module_0.is_quoted(str_2)
        str_3 = ''
        var_3 = module_0.is_quoted(str_3)

if __name__ == "__main__":
    unittest.main()
