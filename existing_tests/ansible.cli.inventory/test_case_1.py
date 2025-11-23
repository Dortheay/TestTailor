import unittest
import timeout_decorator
import ansible.cli.inventory as module_0

class Test_Inventory_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\xa5\xd2\xa09\x9a\x07\x9d\x82\xbdV,,j\xdf\xce'
            str_0 = 'ZO|EOzzdp7~\tc&jq'
            inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
            var_0 = inventory_c_l_i_0.post_process_args(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
