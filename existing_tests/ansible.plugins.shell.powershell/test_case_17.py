import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = None
            bytes_0 = None
            bytes_1 = b'\x1f\x08\xe67\xd9\xfb\xe9\xf5\xcd\xbe\xfd\xd8D\xec \x03qV\x97'
            shell_module_0 = module_0.ShellModule()
            var_0 = shell_module_0.set_user_facl(str_0, bytes_0, bytes_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
