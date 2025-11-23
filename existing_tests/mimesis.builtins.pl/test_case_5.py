import unittest
import timeout_decorator
import mimesis.builtins.pl as module_0
import mimesis.enums as module_1
import datetime as module_2

class Test_Pl_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'oKd7v'
            poland_spec_provider_0 = module_0.PolandSpecProvider(str_0)
            list_0 = []
            str_1 = 'wo\x0c1i#LCFN?I;tuE4-B'
            str_2 = poland_spec_provider_0.pesel(list_0, str_1)
            str_3 = poland_spec_provider_0.pesel()
            poland_spec_provider_1 = module_0.PolandSpecProvider()
            str_4 = poland_spec_provider_1.pesel()
            str_5 = poland_spec_provider_1.nip()
            gender_0 = module_1.Gender.FEMALE
            str_6 = poland_spec_provider_1.pesel(gender_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
