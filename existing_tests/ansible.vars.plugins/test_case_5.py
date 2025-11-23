import unittest
import timeout_decorator
import ansible.vars.plugins as module_0
import ansible.inventory.host as module_1

class Test_Plugins_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            tuple_0 = ()
            bytes_0 = None
            set_0 = {tuple_0, bytes_0}
            float_0 = 369.4291
            var_0 = module_0.get_vars_from_inventory_sources(tuple_0, set_0, tuple_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
