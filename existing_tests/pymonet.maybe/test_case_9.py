import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        list_0 = []
        object_0 = module_1.object(*list_0)
        bool_0 = False
        bool_1 = False
        maybe_0 = module_0.Maybe(bool_0, bool_1)
        bool_2 = maybe_0.__eq__(object_0)

if __name__ == "__main__":
    unittest.main()
