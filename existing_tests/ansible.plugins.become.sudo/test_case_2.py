import unittest
import timeout_decorator
import ansible.plugins.become.sudo as module_0

class Test_Sudo_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            become_module_0 = module_0.BecomeModule()
            become_module_1 = module_0.BecomeModule()
            var_0 = become_module_1.build_become_command(become_module_0, become_module_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
