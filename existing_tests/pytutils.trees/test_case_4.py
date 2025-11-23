import unittest
import timeout_decorator
import pytutils.trees as module_0

class Test_Trees_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
            registry_tree_0 = module_0.RegistryTree()
            var_0 = module_0.set_tree_node(bool_0, dict_0, registry_tree_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
