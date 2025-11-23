import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = 's..N$R}3Pzv]q.UP0'
            float_0 = None
            list_0 = [str_0, float_0, str_0, float_0]
            set_0 = set()
            bool_0 = True
            bytes_0 = b"\xaa\xe5\xf4\xd9H\xb856\xf40\xcd'\xf1?"
            doc_c_l_i_0 = module_0.DocCLI(bytes_0)
            var_0 = doc_c_l_i_0.add_fields(str_0, list_0, set_0, list_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
