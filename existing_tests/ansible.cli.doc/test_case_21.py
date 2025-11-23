import unittest
import timeout_decorator
import ansible.cli.doc as module_0

class Test_Doc_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            dict_0 = None
            set_0 = set()
            list_0 = [set_0, dict_0, set_0, set_0]
            plugin_not_found_0 = module_0.PluginNotFound(*list_0)
            role_mixin_0 = module_0.RoleMixin()
            tuple_0 = (list_0, role_mixin_0)
            var_0 = module_0.jdump(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
