import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        bool_0 = False
        shell_module_0 = module_0.ShellModule()
        bool_1 = False
        var_0 = shell_module_0.wrap_for_exec(bool_1)
        var_1 = shell_module_0.expand_user(bool_0)

if __name__ == "__main__":
    unittest.main()
