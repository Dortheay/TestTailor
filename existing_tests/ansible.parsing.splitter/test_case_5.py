import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'C@=;).8=!v:,MG'
        var_0 = module_0.parse_kv(str_0)
        var_1 = module_0.parse_kv(str_0)
        int_0 = 2875
        var_2 = module_0.parse_kv(str_0, int_0)
        bytes_0 = b'\x0c\x8c\xb2\xc0L>aG\xccq\xd1\xeb\x91\x9e\xd7\x9a\xab\xa21\n'
        var_3 = module_0.parse_kv(bytes_0)

if __name__ == "__main__":
    unittest.main()
