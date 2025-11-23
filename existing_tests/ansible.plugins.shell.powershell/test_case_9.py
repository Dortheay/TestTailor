import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        shell_module_0 = module_0.ShellModule()
        str_0 = 'path/to/script.ps1'
        var_0 = shell_module_0.get_remote_filename(str_0)
        str_1 = 'path/to/program.exe'
        var_1 = shell_module_0.get_remote_filename(str_1)
        str_2 = 'path/to/file.txt'
        var_2 = shell_module_0.get_remote_filename(str_2)
        str_3 = '  path/to/ testfile  '
        var_3 = shell_module_0.get_remote_filename(str_3)

if __name__ == "__main__":
    unittest.main()
