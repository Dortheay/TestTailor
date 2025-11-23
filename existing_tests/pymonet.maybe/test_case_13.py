import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'a\\oJgL#3'
        bool_0 = True
        str_1 = 'D]3)l{EUPKj\n\t'
        str_2 = 'f\\'
        dict_0 = {str_0: str_0, str_1: bool_0, str_2: str_0}
        dict_1 = None
        maybe_0 = module_0.Maybe(dict_1, bool_0)
        maybe_1 = module_0.Maybe(dict_0, bool_0)
        var_0 = maybe_1.to_try()
        var_1 = maybe_1.to_either()
        maybe_2 = module_0.Maybe(str_0, bool_0)
        var_2 = maybe_1.to_lazy()
        var_3 = maybe_2.to_lazy()
        var_4 = None
        var_5 = maybe_2.get_or_else(var_4)
        var_6 = maybe_2.to_box()

if __name__ == "__main__":
    unittest.main()
