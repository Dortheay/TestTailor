import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            bytes_0 = b'u'
            dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
            bool_0 = False
            int_0 = -1340
            doc_c_l_i_0 = module_0.DocCLI(int_0)
            tuple_0 = (bool_0, doc_c_l_i_0)
            str_0 = '\r#/%BGBpDvIk-'
            dict_1 = {str_0: str_0, str_0: str_0}
            doc_c_l_i_1 = module_0.DocCLI(dict_1)
            doc_c_l_i_2 = module_0.DocCLI(doc_c_l_i_1)
            var_0 = doc_c_l_i_2.format_snippet(doc_c_l_i_1, dict_0, tuple_0)
            str_1 = ' .wrp m#;f!1<&O'
            doc_c_l_i_3 = module_0.DocCLI(str_1)
            str_2 = '(?:sun\\w+\\s+)?'
            str_3 = 'lw['
            float_0 = None
            str_4 = ',qVa\\EG,Jh1='
            str_5 = '0f.M?%p"aHCh[^8]Rf.'
            bool_1 = True
            list_0 = [bool_1]
            var_1 = doc_c_l_i_1.find_plugins(str_5, bool_1, list_0)
            dict_2 = {str_2: str_0, str_3: tuple_0, str_3: float_0, str_4: dict_0}
            var_2 = doc_c_l_i_1.get_man_text(dict_2, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
