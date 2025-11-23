import unittest
import timeout_decorator
import ansible.modules.systemd as module_0

class Test_Systemd_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'E@M7DH2, '
            int_0 = 3830
            dict_0 = {str_0: str_0, str_0: int_0, str_0: str_0}
            var_0 = module_0.is_deactivating_service(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
