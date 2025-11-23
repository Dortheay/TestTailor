import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b'\xe6F\xea\x9e\x8a4\xd3\xc2\x1d\xc6'
        list_0 = None
        str_0 = 'run_tags'
        doc_c_l_i_0 = module_0.DocCLI(bytes_0)
        var_0 = doc_c_l_i_0.format_snippet(bytes_0, list_0, str_0)
        role_mixin_0 = module_0.RoleMixin()

if __name__ == "__main__":
    unittest.main()
