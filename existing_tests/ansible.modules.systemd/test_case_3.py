import unittest
import timeout_decorator
import ansible.modules.systemd as module_0

class Test_Systemd_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'oJ/Y56|@Waf'
            str_1 = 'I[M!-}\t`K0r4C\x0bRcj '
            set_0 = {str_0, str_0, str_1, str_0}
            var_0 = module_0.request_was_ignored(set_0)
            var_1 = module_0.is_running_service(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
