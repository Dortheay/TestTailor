import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            tuple_0 = None
            shell_module_0 = module_0.ShellModule()
            var_0 = shell_module_0.path_has_trailing_slash(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
