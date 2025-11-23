import unittest
import timeout_decorator
import ansible.modules.systemd as module_0

class Test_Systemd_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b''
            var_0 = module_0.request_was_ignored(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
