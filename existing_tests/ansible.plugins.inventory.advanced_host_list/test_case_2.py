import unittest
import timeout_decorator
import ansible.plugins.inventory.advanced_host_list as module_0

class Test_Advanced_host_list_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            inventory_module_0 = module_0.InventoryModule()
            str_0 = 'usage: async_wrapper <jid> <time_limit> <modulescript> <argsfile> [-preserve_tmp]  Humans, do not call directly!'
            var_0 = inventory_module_0.verify_file(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
