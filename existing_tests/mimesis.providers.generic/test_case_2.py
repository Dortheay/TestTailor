import unittest
import timeout_decorator
import mimesis.providers.generic as module_0

class Test_Generic_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            generic_0 = module_0.Generic()
            str_0 = '" ,}N'
            generic_0.add_provider(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
