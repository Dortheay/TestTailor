import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        complex_0 = None
        bytes_0 = b'i\xaa\xb7\xafAf\xc0\xe7\xf6\xd4\x15\xb9'
        bool_0 = True
        maybe_0 = module_0.Maybe(bytes_0, bool_0)
        var_0 = maybe_0.ap(complex_0)
        str_0 = '6%3&rx^g~WI'
        str_1 = 'mz|~'
        dict_0 = {str_1: str_1}
        bool_1 = False
        maybe_1 = module_0.Maybe(dict_0, bool_1)
        var_1 = maybe_1.get_or_else(str_0)

if __name__ == "__main__":
    unittest.main()
