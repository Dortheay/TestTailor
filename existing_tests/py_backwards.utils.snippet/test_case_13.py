import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.utils.snippet as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        name_0 = module_0.Name()
        str_0 = "Mm1{'yz#9%1"
        str_1 = 'email.MIMEMultipart'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1, str_1: str_0}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        name_1 = variables_replacer_0.visit_Name(name_0)

if __name__ == "__main__":
    unittest.main()
