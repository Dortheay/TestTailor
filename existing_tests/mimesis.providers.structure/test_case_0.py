import unittest
import timeout_decorator
import mimesis.providers.structure as module_0

class Test_Structure_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        structure_0 = module_0.Structure()
        str_0 = structure_0.html()

if __name__ == "__main__":
    unittest.main()
