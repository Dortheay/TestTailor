import unittest
import timeout_decorator
import ansible.plugins.inventory.yaml as module_0

class Test_Yaml_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'LZDV6Ax/'
            dict_0 = {str_0: str_0}
            str_1 = ']aHd>Qer|:?b@l\t'
            inventory_module_0 = module_0.InventoryModule()
            var_0 = inventory_module_0.parse(dict_0, str_1, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
