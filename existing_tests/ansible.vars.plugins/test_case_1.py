import unittest
import timeout_decorator
import ansible.vars.plugins as module_0
import ansible.inventory.host as module_1

class Test_Plugins_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = -2318
            str_0 = 'MLAxnL;/G8'
            tuple_0 = ()
            var_0 = module_0.get_vars_from_inventory_sources(int_0, str_0, str_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
