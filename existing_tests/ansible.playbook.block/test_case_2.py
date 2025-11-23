import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        float_0 = 624.72
        tuple_0 = ()
        list_0 = []
        list_1 = [tuple_0, list_0, tuple_0, tuple_0]
        block_0 = module_0.Block()
        list_2 = [list_1]
        block_1 = module_0.Block(block_0, list_2)
        float_1 = 2128.8
        block_2 = module_0.Block(tuple_0, list_1, block_1, float_1)
        var_0 = block_2.copy(float_0)

if __name__ == "__main__":
    unittest.main()
