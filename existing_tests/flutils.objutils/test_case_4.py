import unittest
import timeout_decorator
import flutils.objutils as module_0

class Test_Objutils_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bool_0 = True
        bool_1 = module_0.has_callables(bool_0)

if __name__ == "__main__":
    unittest.main()
