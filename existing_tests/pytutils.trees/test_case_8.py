import unittest
import timeout_decorator
import pytutils.trees as module_0

class Test_Trees_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            list_0 = []
            bytes_0 = b''
            registry_tree_0 = module_0.RegistryTree(bytes_0)
            tree_0 = module_0.Tree(list_0)
            str_0 = '\rk\nl}S;'
            var_0 = module_0.tree()
            set_0 = set()
            bool_0 = False
            var_1 = tree_0.__getitem__(set_0, bool_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
