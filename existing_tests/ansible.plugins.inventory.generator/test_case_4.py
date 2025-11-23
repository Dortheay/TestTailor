import unittest
import timeout_decorator
import ansible.plugins.inventory.generator as module_0

class Test_Generator_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = 1118.4
            dict_0 = {float_0: float_0}
            str_0 = '/D^I9|*A<eRm^u>3'
            bytes_0 = b'\xd4\\\xe3\x97\xa8\x90\x1a\xac'
            float_1 = 4147.0
            inventory_module_0 = module_0.InventoryModule()
            var_0 = inventory_module_0.add_parents(dict_0, str_0, bytes_0, float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
