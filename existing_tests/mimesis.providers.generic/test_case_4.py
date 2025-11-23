import unittest
import timeout_decorator
import mimesis.providers.generic as module_0

class Test_Generic_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            generic_0 = module_0.Generic()
            str_0 = '-0oh4T=|tc^-lmK'
            list_0 = [str_0]
            generic_0.add_providers(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
