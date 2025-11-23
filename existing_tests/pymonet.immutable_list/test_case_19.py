import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'mM\tcF@t\r+>q5g%J$i'
        str_1 = 'Box[U]'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0, str_0: str_1}
        immutable_list_0 = module_0.ImmutableList(dict_0)
        var_0 = immutable_list_0.to_list()

if __name__ == "__main__":
    unittest.main()
