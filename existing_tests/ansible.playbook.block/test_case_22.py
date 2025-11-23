import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        list_0 = None
        bool_0 = True
        tuple_0 = (list_0, bool_0)
        block_0 = module_0.Block()
        block_1 = module_0.Block(tuple_0, list_0, block_0)
        var_0 = block_1.serialize()
        float_0 = None
        dict_0 = {float_0: float_0, float_0: float_0}
        tuple_1 = (dict_0,)
        block_2 = module_0.Block(float_0, tuple_1)
        bytes_0 = b'\x1f\xf2Uj\xfc'
        list_1 = [bytes_0, bytes_0, bytes_0, bytes_0]
        var_1 = block_0.serialize()
        list_2 = [list_1, list_1]
        str_0 = '-(_Wc+kJE'
        bool_1 = False
        block_3 = module_0.Block(list_2, str_0, bool_1, bool_1)
        var_2 = block_3.is_block(block_2)
        str_1 = None
        int_0 = -824
        bool_2 = False
        set_0 = {str_1, bool_2, str_1}
        bytes_1 = None
        tuple_2 = (bool_2, set_0, bytes_1)
        block_4 = module_0.Block(int_0, tuple_2)
        bool_3 = True
        block_5 = module_0.Block(bool_3)
        var_3 = block_5.__ne__(block_4)
        var_4 = block_1.set_loader(int_0)

if __name__ == "__main__":
    unittest.main()
