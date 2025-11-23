import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        block_0 = module_0.Block()
        var_0 = block_0.get_include_params()
        list_0 = []
        bool_0 = True
        block_1 = module_0.Block(list_0, block_0, bool_0)
        var_1 = block_1.get_first_parent_include()

if __name__ == "__main__":
    unittest.main()
