import unittest
import timeout_decorator
import pytutils.trees as module_0

class Test_Trees_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            registry_tree_0 = module_0.RegistryTree()
            list_0 = []
            bytes_0 = b''
            registry_tree_1 = module_0.RegistryTree(bytes_0)
            tree_0 = module_0.Tree(list_0)
            var_0 = module_0.tree()
            registry_tree_2 = module_0.RegistryTree()
            bool_0 = None
            list_1 = [bytes_0, bool_0]
            str_0 = 'c))V6+\n:)Y MU\n;\ng;q9'
            float_0 = -3380.66891
            registry_tree_3 = module_0.RegistryTree(list_1, str_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
