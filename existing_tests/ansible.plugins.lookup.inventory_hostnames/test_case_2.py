import unittest
import timeout_decorator
import ansible.plugins.lookup.inventory_hostnames as module_0

class Test_Inventory_hostnames_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'all:!www'
        str_1 = 'groups'
        str_2 = 'all'
        str_3 = 'www'
        str_4 = 'host1'
        str_5 = 'host2'
        str_6 = [str_4, str_5]
        str_7 = [str_5]
        str_8 = {str_2: str_6, str_3: str_7}
        str_9 = {str_1: str_8}
        var_0 = None
        lookup_module_0 = module_0.LookupModule(var_0)
        var_1 = lookup_module_0.run(str_0, str_9)

if __name__ == "__main__":
    unittest.main()
