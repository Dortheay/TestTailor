import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = 'B\tE#h|O@}G8^P@?'
        dict_0 = {str_0: str_0}
        expr_0 = module_1.expr(**dict_0)
        dict_1 = {}
        str_1 = 'typing.Deque'
        str_2 = 'C'
        str_3 = '\n<a id="{}"></a>'
        str_4 = 'VRh0aym?\t5TtS~ <l|B'
        str_5 = '\\'
        str_6 = 'b9.Vj'
        dict_2 = {str_1: str_1, str_2: str_2, str_3: str_4, str_5: str_6}
        parser_0 = module_0.Parser(dict_1, dict_2)
        str_7 = parser_0.resolve(str_0, expr_0)

if __name__ == "__main__":
    unittest.main()
