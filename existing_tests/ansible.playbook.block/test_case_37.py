import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_38(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            float_0 = -1472.820717
            tuple_0 = ()
            str_0 = 'r\t'
            block_0 = module_0.Block(str_0)
            dict_0 = {str_0: tuple_0, float_0: str_0}
            var_0 = block_0.all_parents_static()
            var_1 = block_0.deserialize(dict_0)
            var_2 = block_0.serialize()
            bytes_0 = b'\x97\x8a\x9c1v\xbd&c\x9e\x1caL\x00\x13\x11'
            str_1 = 'Ne7N[a\n7R\tR!'
            int_0 = -1288
            list_0 = [str_0, float_0, str_1, int_0]
            block_1 = module_0.Block(str_1, list_0)
            var_3 = block_1.filter_tagged_tasks(bytes_0)
            dict_1 = {float_0: float_0}
            block_2 = module_0.Block(dict_1)
            var_4 = block_2.copy(tuple_0)
            str_2 = ''
            bool_0 = None
            var_5 = block_2.has_tasks()
            var_6 = block_2.get_include_params()
            var_7 = block_2.get_include_params()
            set_0 = {var_1, float_0}
            var_8 = block_0.load(dict_1, block_0, bool_0, str_2, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
