import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'hf\xfe\xb3PN='
            var_0 = module_0.parse_kv(bytes_0)
            str_0 = 'E\tpI|y\\"|-}L/KZm'
            var_1 = module_0.parse_kv(str_0)
            bytes_1 = b'\x1a\x16\xa2\xec.wurJ5Lf\xe7\xf3\xa6D\xda\xd7'
            var_2 = module_0.split_args(bytes_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
