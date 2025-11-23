import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            dict_0 = {}
            int_0 = 1027
            shell_module_0 = module_0.ShellModule()
            var_0 = shell_module_0.remove(dict_0, int_0)
            bytes_0 = b'\x16\x95k37\xceN'
            str_0 = "'wmE0=p+CHDv\r4O!"
            var_1 = shell_module_0.chmod(bytes_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
