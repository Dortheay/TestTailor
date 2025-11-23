import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = None
            var_0 = module_0.parse_kv(str_0, str_0)
            bool_0 = None
            var_1 = module_0.parse_kv(bool_0)
            str_1 = 'j~Op\t}y '
            float_0 = 800.947623
            var_2 = module_0.parse_kv(str_1, float_0)
            tuple_0 = ()
            str_2 = ';'
            var_3 = module_0.parse_kv(tuple_0, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
