import unittest
import timeout_decorator
import flutils.objutils as module_0

class Test_Objutils_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        bool_0 = True
        str_0 = 'Y4T],J+yq~v0}kJ.;r3'
        list_0 = [str_0, str_0, str_0]
        bool_1 = module_0.has_callables(bool_0, *list_0)

if __name__ == "__main__":
    unittest.main()
