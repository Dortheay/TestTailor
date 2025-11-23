import unittest
import timeout_decorator
import ansible.modules.debconf as module_0

class Test_Debconf_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'ansible.plugins.callback'
            bool_0 = True
            var_0 = module_0.get_selections(str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
