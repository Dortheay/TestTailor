import unittest
import timeout_decorator
import types as module_0
import flutils.namedtupleutils as module_1
import collections as module_2

class Test_Namedtupleutils_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        int_0 = 2131
        str_0 = 'Mfp#"g'
        str_1 = None
        dict_0 = {str_0: int_0, str_0: str_0, str_1: str_1}
        str_2 = '<p(|9/WRKm)c!I:'
        dict_1 = {str_2: str_2}
        list_0 = [dict_1, dict_0, str_1]
        var_0 = module_1.to_namedtuple(list_0)

if __name__ == "__main__":
    unittest.main()
