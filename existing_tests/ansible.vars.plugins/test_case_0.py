import unittest
import timeout_decorator
import ansible.vars.plugins as module_0

class Test_Plugins_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = -2318
        str_0 = 'MLxL;/G8'
        tuple_0 = ()
        dict_0 = {str_0: tuple_0, tuple_0: tuple_0}
        bytes_0 = b''
        var_0 = module_0.get_vars_from_inventory_sources(dict_0, bytes_0, tuple_0, int_0)

if __name__ == "__main__":
    unittest.main()
