import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        block_0 = module_0.Block()
        var_0 = block_0.get_dep_chain()

if __name__ == "__main__":
    unittest.main()
