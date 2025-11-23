import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        tuple_0 = ()
        block_0 = module_0.Block(tuple_0)
        var_0 = block_0.serialize()

if __name__ == "__main__":
    unittest.main()
