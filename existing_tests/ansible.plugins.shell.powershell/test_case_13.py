import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            list_0 = []
            shell_module_0 = module_0.ShellModule()
            var_0 = shell_module_0.join_path(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
