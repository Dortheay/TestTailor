import unittest
import timeout_decorator
import mimesis.providers.generic as module_0

class Test_Generic_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            generic_0 = module_0.Generic()
            var_0 = generic_0.person
            var_1 = generic_0.address
            var_2 = generic_0.non_existent
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
