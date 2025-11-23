import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'uwApH\rQgGF6lqy9'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [str_0, str_0]
        str_1 = '0/.{=&y:^8'
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.remove(dict_0)
        shell_module_1 = module_0.ShellModule()
        dict_1 = {}
        var_1 = shell_module_1.build_module_command(list_0, dict_1, str_1, str_1)

if __name__ == "__main__":
    unittest.main()
