import unittest
import timeout_decorator
import mimesis.builtins.en as module_0
import builtins as module_1

class Test_En_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        u_s_a_spec_provider_0 = module_0.USASpecProvider()

if __name__ == "__main__":
    unittest.main()
