import unittest
import timeout_decorator
import mimesis.providers.generic as module_0

class Test_Generic_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            generic_0 = module_0.Generic()
            list_0 = generic_0.__dir__()
            str_0 = 'KxvOAb\x0cq$q?KVzW*'
            any_0 = generic_0.__getattr__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
