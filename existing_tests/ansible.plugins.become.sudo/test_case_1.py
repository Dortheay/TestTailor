import unittest
import timeout_decorator
import ansible.plugins.become.sudo as module_0

class Test_Sudo_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        become_module_0 = module_0.BecomeModule()
        dict_0 = {}
        int_0 = -1857
        var_0 = become_module_0.build_become_command(dict_0, int_0)

if __name__ == "__main__":
    unittest.main()
