import unittest
import timeout_decorator
import flutils.objutils as module_0

class Test_Objutils_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = None
        bool_0 = module_0.is_list_like(int_0)

if __name__ == "__main__":
    unittest.main()
