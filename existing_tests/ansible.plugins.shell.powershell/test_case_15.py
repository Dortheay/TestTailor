import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            shell_module_0 = module_0.ShellModule()
            bool_0 = True
            dict_0 = {shell_module_0: bool_0, shell_module_0: shell_module_0, bool_0: bool_0, bool_0: bool_0}
            str_0 = '<~@)!4R):N3o+b32S_94'
            bytes_0 = b'\xa8\xb6?\xc6u'
            dict_1 = {str_0: dict_0, str_0: bytes_0, str_0: shell_module_0}
            var_0 = shell_module_0.exists(dict_1)
            var_1 = shell_module_0.chmod(dict_0, shell_module_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
