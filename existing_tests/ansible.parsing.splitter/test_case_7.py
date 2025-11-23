import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'key1=value1 key2=value2'
        var_0 = module_0.parse_kv(str_0)
        str_1 = 'key1="value 1" key2=\'value 2\''
        var_1 = module_0.parse_kv(str_1)
        str_2 = 'key1=value\\=1 key2=value2'
        var_2 = module_0.parse_kv(str_2)
        str_3 = 'freekey freevalue key1=value1'
        bool_0 = True
        var_3 = module_0.parse_kv(str_3, bool_0)
        str_4 = ''
        var_4 = module_0.parse_kv(str_4)
        str_5 = 'creates=/tmp/file key=value removes=/tmp/otherfile'
        var_5 = module_0.parse_kv(str_5, bool_0)

if __name__ == "__main__":
    unittest.main()
