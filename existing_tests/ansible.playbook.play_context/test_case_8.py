import unittest
import timeout_decorator
import ansible.playbook.play_context as module_0

class Test_Play_context_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            dict_0 = {}
            play_context_0 = module_0.PlayContext()
            bool_0 = False
            play_context_1 = module_0.PlayContext(bool_0)
            var_0 = play_context_1.set_become_plugin(play_context_0)
            play_context_2 = module_0.PlayContext()
            var_1 = play_context_2.update_vars(dict_0)
            var_2 = play_context_1.update_vars(dict_0)
            play_context_3 = module_0.PlayContext()
            play_context_4 = module_0.PlayContext(play_context_3)
            var_3 = play_context_4.set_attributes_from_cli()
            float_0 = 956.6892322930726
            var_4 = play_context_4.set_become_plugin(play_context_3)
            str_0 = '-search'
            var_5 = play_context_4.set_task_and_variable_override(play_context_4, float_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
