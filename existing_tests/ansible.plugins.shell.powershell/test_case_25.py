import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            shell_module_0 = module_0.ShellModule()
            str_0 = 'C:/Users/Example/'
            var_0 = shell_module_0.path_has_trailing_slash(str_0)
            int_0 = -706
            float_0 = 640.709
            float_1 = 0.1
            var_1 = shell_module_0.build_module_command(int_0, float_0, float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
