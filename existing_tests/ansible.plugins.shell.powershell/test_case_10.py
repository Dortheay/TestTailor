import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        shell_module_0 = module_0.ShellModule()
        str_0 = "$env:TEST_VAR='test_value';"
        str_1 = '#!powershel('
        str_2 = 'test_script'
        var_0 = None
        var_1 = shell_module_0.build_module_command(str_0, str_1, str_2, var_0)

if __name__ == "__main__":
    unittest.main()
