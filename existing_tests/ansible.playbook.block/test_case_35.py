import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_36(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            set_0 = set()
            float_0 = 149.8
            str_0 = 'eP\tUm}'
            block_0 = module_0.Block(str_0)
            float_1 = -511.258
            block_1 = module_0.Block(block_0, block_0, float_1)
            var_0 = block_1.copy()
            var_1 = block_0.get_dep_chain()
            var_2 = block_0.preprocess_data(float_0)
            var_3 = block_0.get_dep_chain()
            var_4 = block_1.has_tasks()
            var_5 = block_1.filter_tagged_tasks(set_0)
            var_6 = block_1.get_dep_chain()
            block_2 = module_0.Block(block_0, block_0)
            var_7 = block_1.serialize()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
