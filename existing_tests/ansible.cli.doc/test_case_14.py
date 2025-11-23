import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = 24
            float_0 = 888.63
            set_0 = {float_0}
            bytes_0 = b'\xc9d\x89\xcc^F\xa0\x9f\x88\x1e\xf4\x89\x8c\xad\xecz'
            bool_0 = False
            bool_1 = True
            bool_2 = False
            list_0 = [bool_2]
            doc_c_l_i_0 = module_0.DocCLI(list_0)
            var_0 = doc_c_l_i_0.format_plugin_doc(int_0, float_0, set_0, bytes_0, bool_0, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
