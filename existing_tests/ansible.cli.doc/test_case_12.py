import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            int_0 = -2488
            doc_c_l_i_0 = module_0.DocCLI(int_0)
            tuple_0 = (doc_c_l_i_0,)
            str_0 = 'CollectionMetadata'
            str_1 = 'nameservers'
            bool_0 = True
            str_2 = None
            dict_0 = {str_0: doc_c_l_i_0, str_0: tuple_0, str_1: bool_0, str_2: int_0}
            str_3 = None
            str_4 = '[@wD'
            str_5 = '\n    Return a copy of dictionaries of variables based on configured hash behavior\n    '
            dict_1 = {str_3: str_3, str_4: str_3, str_5: str_5}
            doc_c_l_i_1 = module_0.DocCLI(dict_1)
            var_0 = doc_c_l_i_1.namespace_from_plugin_filepath(tuple_0, str_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
