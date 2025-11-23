import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        object_0 = module_1.object()
        list_0 = []
        either_0 = module_0.Either(list_0)
        bool_0 = either_0.__eq__(object_0)

if __name__ == "__main__":
    unittest.main()
