import unittest
import timeout_decorator
import types as module_0
import flutils.namedtupleutils as module_1
import collections as module_2

class Test_Namedtupleutils_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        simple_namespace_0 = module_0.SimpleNamespace()
        var_0 = module_1.to_namedtuple(simple_namespace_0)
        list_0 = [var_0, simple_namespace_0]
        var_1 = module_1.to_namedtuple(list_0)

if __name__ == "__main__":
    unittest.main()
