import unittest
import timeout_decorator
import ansible.plugins.inventory.toml as module_0

class Test_Toml_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        set_0 = set()
        list_0 = [set_0, set_0, set_0]
        list_1 = [list_0, set_0]
        list_2 = [list_1, set_0, list_1, set_0]
        var_0 = module_0.convert_yaml_objects_to_native(list_2)

if __name__ == "__main__":
    unittest.main()
