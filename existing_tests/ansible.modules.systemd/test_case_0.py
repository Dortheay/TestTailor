import unittest
import timeout_decorator
import ansible.modules.systemd as module_0

class Test_Systemd_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\xe9\x80\xe2\x04\xfc\xee\xe6\xd4\xb9\xc2\xb9\xe5\xf3H\xac\xaf&\x9d'
            var_0 = module_0.is_running_service(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
