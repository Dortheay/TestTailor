import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        set_0 = set()
        float_0 = 149.8
        str_0 = 'eP\tUm}'
        block_0 = module_0.Block(str_0)
        float_1 = -511.258
        block_1 = module_0.Block(block_0, block_0, float_1)
        var_0 = block_1.copy()
        bytes_0 = b'3c\xfd;Zz\xac'
        tuple_0 = (block_1, bytes_0, set_0)
        var_1 = block_0.get_dep_chain()
        var_2 = block_0.preprocess_data(float_0)
        var_3 = block_0.get_dep_chain()
        str_1 = 'Gq5ewL=2@'
        var_4 = block_0.filter_tagged_tasks(str_1)
        var_5 = block_1.get_dep_chain()
        block_2 = module_0.Block(tuple_0)

if __name__ == "__main__":
    unittest.main()
