import unittest
import timeout_decorator
import mimesis.providers.generic as module_0

class Test_Generic_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        generic_0 = module_0.Generic()

if __name__ == "__main__":
    unittest.main()
