import unittest
import timeout_decorator
import ansible.plugins.become.su as module_0

class Test_Su_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'prompt_l10n'
            str_1 = 'Contraseña'
            become_module_0 = module_0.BecomeModule()
            var_0 = become_module_0.set_option(str_0, str_1)
            str_2 = 'Contraseña :'
            var_1 = become_module_0.check_password_prompt(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
