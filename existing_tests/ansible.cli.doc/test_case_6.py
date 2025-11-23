import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = ' .wr m#;f!1<&O'
            doc_c_l_i_0 = module_0.DocCLI(str_0)
            var_0 = doc_c_l_i_0.run()
            tuple_0 = ()
            doc_c_l_i_1 = module_0.DocCLI(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
