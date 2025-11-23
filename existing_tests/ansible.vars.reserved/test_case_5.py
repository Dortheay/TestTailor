import unittest
import timeout_decorator
import ansible.vars.reserved as module_0

class Test_Reserved_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = 0.5
            var_0 = module_0.warn_if_reserved(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
