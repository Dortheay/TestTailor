import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'key1=value1 key2=value2'
        var_0 = module_0.parse_kv(str_0)
        str_1 = 'key1=val\\=ue1 key2=value\\ space'
        var_1 = module_0.parse_kv(str_1)
        str_2 = 'key1=value1 freeformparam'
        var_2 = module_0.parse_kv(str_2)
        str_3 = 'key1=value1 freeformparam'
        bool_0 = True
        var_3 = module_0.parse_kv(str_3, bool_0)
        str_4 = 'key\\=escaped=val\\=ue key2=value2'
        var_4 = module_0.parse_kv(str_4)
        str_5 = ''
        var_5 = module_0.parse_kv(str_5)
        str_6 = 'key1:value1'
        var_6 = module_0.parse_kv(str_6)

if __name__ == "__main__":
    unittest.main()
