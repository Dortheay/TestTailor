import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = ":X\n)'-.$\\wW"
            dict_0 = None
            shell_module_0 = module_0.ShellModule()
            var_0 = shell_module_0.chown(str_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
