import unittest
import timeout_decorator
import mimesis.builtins.pl as module_0
import mimesis.enums as module_1
import datetime as module_2

class Test_Pl_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = -769.474585
            poland_spec_provider_0 = module_0.PolandSpecProvider()
            poland_spec_provider_1 = module_0.PolandSpecProvider()
            str_0 = poland_spec_provider_1.pesel(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
