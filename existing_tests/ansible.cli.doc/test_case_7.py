import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            role_mixin_0 = module_0.RoleMixin()
            set_0 = {role_mixin_0, role_mixin_0}
            str_0 = 'V['
            str_1 = 'Nwz/%vi^7\\]|'
            str_2 = 'W+d'
            int_0 = 1382
            str_3 = "(u9q!a,NU'q@2y/A=d1p"
            str_4 = "}'-4M^!"
            dict_0 = {str_0: str_0, str_1: str_0, str_2: int_0, str_3: str_4}
            doc_c_l_i_0 = module_0.DocCLI(dict_0)
            var_0 = doc_c_l_i_0.post_process_args(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
