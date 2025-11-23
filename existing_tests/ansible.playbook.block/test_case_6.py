import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        block_0 = module_0.Block()
        var_0 = block_0.filter_tagged_tasks(block_0)

if __name__ == "__main__":
    unittest.main()
