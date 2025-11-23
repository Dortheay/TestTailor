import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            shell_module_0 = module_0.ShellModule()
            shell_module_1 = module_0.ShellModule()
            var_0 = shell_module_1.env_prefix()
            set_0 = set()
            bytes_0 = b"\xbb\x89a'\xddQ\x197\x00\x7f(9"
            var_1 = shell_module_0.chown(set_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
