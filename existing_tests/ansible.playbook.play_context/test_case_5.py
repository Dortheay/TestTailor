import unittest
import timeout_decorator
import ansible.playbook.play_context as module_0

class Test_Play_context_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            dict_0 = {}
            play_context_0 = module_0.PlayContext()
            var_0 = play_context_0.update_vars(dict_0)
            play_context_1 = module_0.PlayContext()
            play_context_2 = module_0.PlayContext(play_context_1)
            var_1 = play_context_2.set_attributes_from_cli()
            float_0 = 956.6892322930726
            var_2 = play_context_2.set_become_plugin(play_context_1)
            str_0 = '-search'
            var_3 = play_context_2.set_task_and_variable_override(play_context_2, float_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
