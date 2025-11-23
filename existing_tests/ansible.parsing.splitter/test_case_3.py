import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'Gmpu>\nXcB~X2nM}'
        str_1 = '=4T*S%kvG6'
        var_0 = module_0.parse_kv(str_0)
        bytes_0 = b''
        var_1 = module_0.parse_kv(bytes_0)
        var_2 = module_0.split_args(str_1)

if __name__ == "__main__":
    unittest.main()
