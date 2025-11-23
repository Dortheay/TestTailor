import unittest
import timeout_decorator
import ansible.vars.plugins as module_0
import ansible.inventory.host as module_1

class Test_Plugins_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = -367
            list_0 = [int_0, int_0, int_0]
            dict_0 = {int_0: int_0, int_0: int_0, int_0: list_0}
            bool_0 = True
            str_0 = 'NkW\x0c{O.s-CA\rq'
            tuple_0 = (bool_0, int_0, str_0, dict_0)
            var_0 = module_0.get_plugin_vars(dict_0, bool_0, int_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
