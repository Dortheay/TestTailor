import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        block_0 = module_0.Block()
        var_0 = block_0.all_parents_static()

if __name__ == "__main__":
    unittest.main()
