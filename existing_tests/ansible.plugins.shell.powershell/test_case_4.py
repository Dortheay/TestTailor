import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        shell_module_0 = module_0.ShellModule()
        str_0 = '#!powershell'
        var_0 = None
        var_1 = shell_module_0.build_module_command(str_0, str_0, str_0, var_0)

if __name__ == "__main__":
    unittest.main()
