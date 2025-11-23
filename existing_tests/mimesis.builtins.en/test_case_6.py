import unittest
import timeout_decorator
import mimesis.builtins.en as module_0

class Test_En_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'KSA'
            u_s_a_spec_provider_0 = module_0.USASpecProvider()
            str_1 = u_s_a_spec_provider_0.ssn()
            str_2 = u_s_a_spec_provider_0.ssn()
            var_0 = u_s_a_spec_provider_0.personality()
            str_3 = u_s_a_spec_provider_0.ssn()
            str_4 = u_s_a_spec_provider_0.tracking_number()
            u_s_a_spec_provider_1 = module_0.USASpecProvider()
            var_1 = u_s_a_spec_provider_1.personality(str_0)
            u_s_a_spec_provider_2 = module_0.USASpecProvider()
            var_2 = u_s_a_spec_provider_2.personality()
            str_5 = u_s_a_spec_provider_0.ssn()
            str_6 = u_s_a_spec_provider_1.tracking_number()
            str_7 = u_s_a_spec_provider_2.ssn()
            u_s_a_spec_provider_3 = module_0.USASpecProvider()
            u_s_a_spec_provider_4 = module_0.USASpecProvider()
            u_s_a_spec_provider_5 = module_0.USASpecProvider()
            str_8 = u_s_a_spec_provider_4.tracking_number()
            str_9 = ',Sg^<eg}!JC['
            str_10 = u_s_a_spec_provider_5.tracking_number(str_9)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
