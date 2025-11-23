import unittest
import timeout_decorator
import pytutils.trees as module_0

class Test_Trees_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        registry_tree_0 = module_0.RegistryTree()
        tree_0 = module_0.Tree(registry_tree_0)

if __name__ == "__main__":
    unittest.main()
