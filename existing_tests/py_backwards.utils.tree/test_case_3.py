import unittest
import timeout_decorator
import py_backwards.utils.tree as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Tree_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 1508
            list_0 = []
            str_0 = 'Fi'
            str_1 = '&nF\rtUxNe8F].J%3\nC'
            str_2 = '!%V_+'
            dict_0 = {str_2: list_0, str_2: str_0}
            a_s_t_0 = module_1.AST(**dict_0)
            float_0 = 533.17819
            iterable_0 = module_0.find(a_s_t_0, float_0)
            dict_1 = {str_0: int_0, str_0: list_0, str_1: list_0, str_1: iterable_0}
            a_s_t_1 = module_1.AST(*list_0, **dict_1)
            module_0.replace_at(int_0, a_s_t_1, a_s_t_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
