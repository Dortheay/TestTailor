import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        block_0 = module_0.Block()
        str_0 = '\x0bb'
        var_0 = block_0.copy()
        block_1 = module_0.Block()
        list_0 = []
        var_1 = block_1.has_tasks()
        var_2 = block_0.set_loader(list_0)
        var_3 = block_1.copy()
        var_4 = block_1.get_dep_chain()
        var_5 = block_0.__repr__()
        var_6 = block_1.has_tasks()
        var_7 = block_1.set_loader(str_0)

if __name__ == "__main__":
    unittest.main()
