import unittest
import timeout_decorator
import ansible.plugins.become.su as module_0

class Test_Su_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b"\xfd\xfd\x90\x07\xba\xe3S\xd7\xa1\xb0\xc8\x13'"
            become_module_0 = module_0.BecomeModule()
            var_0 = become_module_0.check_password_prompt(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
