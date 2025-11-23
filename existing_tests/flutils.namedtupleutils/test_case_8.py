import unittest
import timeout_decorator
import types as module_0
import flutils.namedtupleutils as module_1
import collections as module_2

class Test_Namedtupleutils_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        int_0 = 173
        str_0 = 'NamedTuple'
        dict_0 = {str_0: int_0, str_0: str_0}
        bool_0 = True
        tuple_0 = (int_0, dict_0, int_0, bool_0)
        var_0 = module_1.to_namedtuple(tuple_0)
        var_1 = module_1.to_namedtuple(tuple_0)
        dict_1 = {str_0: str_0}
        str_1 = 'I?pC.'
        list_0 = [dict_1, var_0, dict_1, str_1]
        var_2 = module_1.to_namedtuple(list_0)

if __name__ == "__main__":
    unittest.main()
