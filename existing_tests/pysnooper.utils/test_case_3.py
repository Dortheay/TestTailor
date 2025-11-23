import unittest
import timeout_decorator
import pysnooper.utils as module_0

class Test_Utils_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bool_0 = False
        bytes_0 = b'8mJ\xf5\x92\xef\x8c@\xfd'
        var_0 = module_0.ensure_tuple(bytes_0)
        int_0 = 2118
        str_0 = 'ge_surce'
        str_1 = None
        str_2 = 'M:P0YY<\t'
        dict_0 = {str_0: bool_0, str_1: int_0, str_0: bool_0, str_2: int_0}
        bytes_1 = b'\x0eI\xc6H\x83\xfa\xc0\x020\n]K\x94\x19'
        var_1 = module_0.truncate(bytes_1, bool_0)
        var_2 = module_0.get_shortish_repr(dict_0)
        var_3 = module_0.ensure_tuple(int_0)
        str_3 = '{}...{}'
        var_4 = module_0.shitcode(str_3)

if __name__ == "__main__":
    unittest.main()
