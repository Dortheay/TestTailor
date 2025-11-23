import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        shell_module_0 = module_0.ShellModule()

if __name__ == "__main__":
    unittest.main()
