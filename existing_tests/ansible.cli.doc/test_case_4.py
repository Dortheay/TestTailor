import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = {}
            role_mixin_0 = module_0.RoleMixin(**dict_0)
            doc_c_l_i_0 = module_0.DocCLI(role_mixin_0)
            complex_0 = None
            var_0 = module_0.jdump(complex_0)
            doc_c_l_i_1 = module_0.DocCLI(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
