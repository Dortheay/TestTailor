import unittest
import timeout_decorator
import ansible.plugins.become.su as module_0

class Test_Su_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '4=^\n'
            become_module_0 = None
            dict_0 = {str_0: str_0, str_0: become_module_0}
            become_module_1 = module_0.BecomeModule()
            var_0 = become_module_1.build_become_command(become_module_0, dict_0)
            become_module_2 = module_0.BecomeModule()
            var_1 = become_module_2.check_password_prompt(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
