import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        shell_module_0 = module_0.ShellModule()
        str_0 = "$env:TEST_VAR='test_calue';"
        str_1 = 'G'
        str_2 = '\x0bZ7'
        var_0 = None
        var_1 = shell_module_0.build_module_command(str_0, str_1, str_2, var_0)

if __name__ == "__main__":
    unittest.main()
