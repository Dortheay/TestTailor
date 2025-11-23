import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        bool_0 = True
        list_0 = [bool_0]
        block_0 = module_0.Block(bool_0)
        var_0 = block_0.get_vars()
        var_1 = block_0.has_tasks()
        int_0 = -2150
        block_1 = module_0.Block(list_0, block_0)
        var_2 = block_1.preprocess_data(block_0)
        block_2 = module_0.Block(int_0)
        var_3 = block_2.all_parents_static()

if __name__ == "__main__":
    unittest.main()
