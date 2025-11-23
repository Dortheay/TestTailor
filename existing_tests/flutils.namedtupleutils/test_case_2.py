import unittest
import timeout_decorator
import types as module_0
import flutils.namedtupleutils as module_1
import collections as module_2

class Test_Namedtupleutils_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'v:ftSOseg\tZ~ \tch'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [dict_0, str_0, str_0, dict_0]
        var_0 = module_1.to_namedtuple(list_0)

if __name__ == "__main__":
    unittest.main()
