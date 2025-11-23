import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            dict_0 = {}
            list_0 = [dict_0, dict_0, dict_0]
            list_1 = [list_0, list_0]
            shell_module_0 = module_0.ShellModule()
            var_0 = shell_module_0.join_path(*list_1)
            shell_module_1 = module_0.ShellModule()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
