import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            int_0 = -4837
            str_0 = '\n    Add options for commands which need to prompt for privilege escalation credentials\n\n    Note that add_runas_options() includes these options already.  Only one of the two functions\n    should be used.\n    '
            int_1 = 4430
            block_0 = module_0.Block(int_1)
            var_0 = block_0.serialize()
            float_0 = -2004.97364
            var_1 = block_0.set_loader(block_0)
            var_2 = block_0.all_parents_static()
            tuple_0 = (str_0, float_0)
            int_2 = 900
            var_3 = block_0.preprocess_data(int_2)
            block_1 = module_0.Block(str_0, tuple_0)
            str_1 = 'K[`B'
            float_1 = -564.13871
            block_2 = module_0.Block(int_0, str_1, float_1)
            int_3 = -3049
            var_4 = block_0.is_block(int_3)
            var_5 = block_2.__repr__()
            var_6 = block_2.has_tasks()
            int_4 = 661
            var_7 = block_1.set_loader(int_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
