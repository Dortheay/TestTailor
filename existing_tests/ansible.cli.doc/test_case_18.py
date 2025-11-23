import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            str_0 = '('
            dict_0 = {str_0: str_0, str_0: str_0}
            bool_0 = False
            bytes_0 = b'\xbc\xa8\xe2\xed.8\x04\xa0iL\x90\\\xd3\xfe-\x8b\xd4'
            int_0 = 1663
            list_0 = [bool_0, dict_0, bytes_0, bytes_0]
            list_1 = []
            role_mixin_0 = module_0.RoleMixin(*list_1)
            doc_c_l_i_0 = module_0.DocCLI(role_mixin_0)
            var_0 = doc_c_l_i_0.get_man_text(dict_0, int_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
