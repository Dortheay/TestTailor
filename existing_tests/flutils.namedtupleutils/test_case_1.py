import unittest
import timeout_decorator
import types as module_0
import flutils.namedtupleutils as module_1
import collections as module_2

class Test_Namedtupleutils_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        dict_0 = None
        list_0 = [dict_0]
        var_0 = module_1.to_namedtuple(list_0)
        list_1 = [var_0, dict_0]
        var_1 = module_1.to_namedtuple(list_1)

if __name__ == "__main__":
    unittest.main()
