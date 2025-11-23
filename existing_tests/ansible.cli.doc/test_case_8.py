import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bytes_0 = None
            role_mixin_0 = module_0.RoleMixin()
            doc_c_l_i_0 = module_0.DocCLI(role_mixin_0)
            var_0 = doc_c_l_i_0.display_plugin_list(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
