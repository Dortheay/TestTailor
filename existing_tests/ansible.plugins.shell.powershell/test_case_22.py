import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            shell_module_0 = module_0.ShellModule()
            bytes_0 = b'\x96(/\xe7\xe5<\x08><\x12)\xfbr\xdc\xbb\xcf\x01\xfa\r'
            shell_module_1 = module_0.ShellModule()
            var_0 = shell_module_1.mkdtemp(shell_module_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
