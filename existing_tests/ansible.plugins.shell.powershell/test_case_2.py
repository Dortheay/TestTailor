import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bool_0 = False
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.expand_user(bool_0)

if __name__ == "__main__":
    unittest.main()
