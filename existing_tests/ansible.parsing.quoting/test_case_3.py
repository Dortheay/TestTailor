import unittest
import timeout_decorator
import ansible.parsing.quoting as module_0

class Test_Quoting_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '"hello"'
        var_0 = module_0.unquote(str_0)
        str_1 = "'world'"
        var_1 = module_0.unquote(str_1)
        str_2 = 'hello'
        var_2 = module_0.unquote(str_2)
        str_3 = '"hello\''
        var_3 = module_0.unquote(str_3)
        str_4 = '"he\\"llo"'
        var_4 = module_0.unquote(str_4)
        str_5 = ''
        var_5 = module_0.unquote(str_5)

if __name__ == "__main__":
    unittest.main()
