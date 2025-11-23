import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            tuple_0 = None
            bool_0 = True
            list_0 = None
            tuple_1 = (tuple_0, tuple_0, bool_0, list_0)
            set_0 = set()
            str_0 = 'W'
            doc_c_l_i_0 = module_0.DocCLI(str_0)
            var_0 = doc_c_l_i_0.get_role_man_text(tuple_1, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
