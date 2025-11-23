import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            shell_module_0 = module_0.ShellModule()
            var_0 = shell_module_0.mkdtemp()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
