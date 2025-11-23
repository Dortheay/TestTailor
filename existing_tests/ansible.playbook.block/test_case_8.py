import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        block_0 = module_0.Block()
        var_0 = block_0.copy(block_0)

if __name__ == "__main__":
    unittest.main()
