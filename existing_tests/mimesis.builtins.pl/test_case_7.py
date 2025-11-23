import unittest
import timeout_decorator
import mimesis.builtins.pl as module_0
import mimesis.enums as module_1
import datetime as module_2

class Test_Pl_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            poland_spec_provider_0 = module_0.PolandSpecProvider()
            str_0 = poland_spec_provider_0.pesel()
            poland_spec_provider_1 = module_0.PolandSpecProvider()
            str_1 = poland_spec_provider_0.nip()
            bytearray_0 = None
            gender_0 = module_1.Gender.FEMALE
            str_2 = poland_spec_provider_0.pesel(bytearray_0, gender_0)
            str_3 = poland_spec_provider_1.nip()
            str_4 = poland_spec_provider_0.nip()
            str_5 = poland_spec_provider_0.regon()
            str_6 = poland_spec_provider_0.nip()
            str_7 = poland_spec_provider_0.nip()
            str_8 = poland_spec_provider_1.regon()
            poland_spec_provider_2 = module_0.PolandSpecProvider()
            str_9 = poland_spec_provider_2.pesel()
            gender_1 = module_1.Gender.MALE
            str_10 = poland_spec_provider_2.pesel()
            datetime_0 = None
            str_11 = poland_spec_provider_2.pesel(datetime_0, gender_1)
            str_12 = poland_spec_provider_2.pesel()
            datetime_1 = module_2.datetime()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
