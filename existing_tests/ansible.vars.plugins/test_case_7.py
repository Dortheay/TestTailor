import unittest
import timeout_decorator
import ansible.vars.plugins as module_0
import ansible.inventory.host as module_1

class Test_Plugins_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = ',Qhq\tY8Pt'
            dict_0 = {}
            var_0 = module_0.get_vars_from_inventory_sources(dict_0, str_0, dict_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
