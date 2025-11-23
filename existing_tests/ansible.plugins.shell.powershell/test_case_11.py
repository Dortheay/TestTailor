import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        shell_module_0 = module_0.ShellModule()
        str_0 = '~'
        var_0 = shell_module_0.expand_user(str_0)
        str_1 = '~\\Documents'
        var_1 = shell_module_0.expand_user(str_1)
        str_2 = 'C:\\Users\\UserName\\Desktop'
        var_2 = shell_module_0.expand_user(str_2)
        str_3 = '\\Program Files'
        var_3 = shell_module_0.expand_user(str_3)

if __name__ == "__main__":
    unittest.main()
