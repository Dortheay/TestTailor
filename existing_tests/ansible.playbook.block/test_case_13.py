import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        bool_0 = True
        block_0 = module_0.Block(bool_0)
        list_0 = []
        block_1 = module_0.Block(block_0)
        var_0 = block_1.filter_tagged_tasks(list_0)

if __name__ == "__main__":
    unittest.main()
