import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        block_0 = module_0.Block()

if __name__ == "__main__":
    unittest.main()
