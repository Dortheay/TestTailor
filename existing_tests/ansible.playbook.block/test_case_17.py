import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        set_0 = set()
        str_0 = '189ba585-3bd6-1099-1640-000000000107'
        bytes_0 = b'n\xf68\xbe\x87\x05\x83\xee\xd3\xe2b\x1aQ\xa5\xe6'
        bool_0 = False
        block_0 = module_0.Block(str_0, bool_0)
        block_1 = module_0.Block(bytes_0, block_0, block_0)
        var_0 = block_1.get_include_params()
        complex_0 = None
        list_0 = [set_0, set_0, str_0, complex_0]
        block_2 = module_0.Block(list_0)
        var_1 = block_2.get_first_parent_include()
        float_0 = 110.60263341186052
        str_1 = 'eP\tm}'
        block_3 = module_0.Block(str_1)
        float_1 = -511.258
        block_4 = module_0.Block(block_3, block_3, float_1)
        var_2 = block_4.copy()
        var_3 = block_3.get_dep_chain()
        var_4 = block_3.preprocess_data(float_0)
        var_5 = block_3.get_dep_chain()
        dict_0 = None
        var_6 = block_1.filter_tagged_tasks(dict_0)

if __name__ == "__main__":
    unittest.main()
