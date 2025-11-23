import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_39(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            float_0 = 149.8
            str_0 = 'eP\tUm}'
            block_0 = module_0.Block(str_0)
            float_1 = -511.258
            block_1 = module_0.Block(block_0, block_0, float_1)
            var_0 = block_1.copy()
            var_1 = block_0.get_dep_chain()
            var_2 = block_0.get_dep_chain()
            str_1 = 's%UE'
            bytes_0 = b'\xfbT\x03\x11\x86\xe9TF\x13[q-_lj\x9d\xb8['
            var_3 = block_0.filter_tagged_tasks(bytes_0)
            var_4 = block_1.get_dep_chain()
            set_0 = None
            str_2 = 'B;y{XUFmAPuXL'
            int_0 = None
            dict_0 = {}
            str_3 = 'uV\x0b#\x0bSae]'
            list_0 = [str_3, bytes_0, dict_0]
            tuple_0 = (str_3, list_0, int_0)
            block_2 = module_0.Block(dict_0, set_0, tuple_0)
            block_3 = module_0.Block(str_2, int_0, block_2)
            block_4 = module_0.Block(tuple_0, block_3)
            tuple_1 = ()
            block_5 = module_0.Block(str_1, float_0, tuple_1)
            var_5 = block_4.serialize()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
