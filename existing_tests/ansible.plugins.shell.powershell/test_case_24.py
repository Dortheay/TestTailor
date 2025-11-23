import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = ''
            shell_module_0 = module_0.ShellModule()
            shell_module_1 = module_0.ShellModule()
            var_0 = shell_module_1.get_remote_filename(str_0)
            dict_0 = {}
            bytes_0 = b';\xd6\xbb\xab\xef\xee\x9f\x00"\xafQ\xf0\xa4\xc3l'
            var_1 = shell_module_0.build_module_command(str_0, bytes_0, str_0)
            shell_module_2 = module_0.ShellModule()
            shell_module_3 = module_0.ShellModule()
            str_1 = '4N5\tbj<f,u]c'
            var_2 = shell_module_2.build_module_command(str_0, str_1, str_1)
            var_3 = shell_module_3.mkdtemp(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
