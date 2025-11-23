import unittest
import timeout_decorator
import mimesis.builtins.en as module_0

class Test_En_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'THk!`,x(X3M'
            u_s_a_spec_provider_0 = module_0.USASpecProvider()
            str_1 = u_s_a_spec_provider_0.tracking_number(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
