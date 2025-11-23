import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = ';<Yc4z9+.X7F'
        shell_module_0 = module_0.ShellModule()
        set_0 = set()
        var_0 = shell_module_0.get_remote_filename(str_0)
        var_1 = shell_module_0.expand_user(set_0)

if __name__ == "__main__":
    unittest.main()
