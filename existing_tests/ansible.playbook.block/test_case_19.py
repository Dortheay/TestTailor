import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        block_0 = module_0.Block()
        var_0 = block_0.serialize()
        var_1 = block_0.get_first_parent_include()

if __name__ == "__main__":
    unittest.main()
