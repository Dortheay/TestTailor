import unittest
import timeout_decorator
import mimesis.providers.generic as module_0

class Test_Generic_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            generic_0 = module_0.Generic()
            generic_0.add_providers()
            tuple_0 = ()
            generic_0.add_provider(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
