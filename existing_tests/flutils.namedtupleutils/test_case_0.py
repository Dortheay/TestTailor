import unittest
import timeout_decorator
import types as module_0
import flutils.namedtupleutils as module_1
import collections as module_2

class Test_Namedtupleutils_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        simple_namespace_0 = module_0.SimpleNamespace()
        var_0 = module_1.to_namedtuple(simple_namespace_0)

if __name__ == "__main__":
    unittest.main()
