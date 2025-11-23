import unittest
import timeout_decorator
import ansible.vars.plugins as module_0
import ansible.inventory.host as module_1

class Test_Plugins_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bool_0 = None
            dict_0 = {}
            bytes_0 = b'\x07U\x07\xf1\xe2\xf2'
            str_0 = ".C\x0b+c+F1\x0c5`A]*rvf%~'"
            list_0 = []
            var_0 = module_0.get_vars_from_inventory_sources(bytes_0, str_0, list_0, bool_0)
            int_0 = 988
            bytes_1 = b'+\xfe^\x07#\x86@\x80\x9bg\xb4jR\xac\xa7\xfd\x10i\xa5\xf7'
            var_1 = module_0.get_vars_from_inventory_sources(list_0, int_0, bytes_1, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
