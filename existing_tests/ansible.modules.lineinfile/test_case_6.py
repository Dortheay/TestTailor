import unittest
import timeout_decorator
import ansible.modules.lineinfile as module_0

class Test_Lineinfile_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bytes_0 = b'A\xe3S\xa4\x80j'
            dict_0 = None
            tuple_0 = None
            set_0 = set()
            str_0 = "zav[/Y,NN'bVbFewit#"
            str_1 = "'`s>D.G0"
            list_0 = [str_1, str_0, set_0]
            bool_0 = True
            int_0 = -2346
            var_0 = module_0.present(set_0, str_0, bytes_0, tuple_0, str_1, dict_0, list_0, bool_0, set_0, set_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
