import unittest
import timeout_decorator
import ansible.playbook.play_context as module_0

class Test_Play_context_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        dict_0 = {}
        play_context_0 = module_0.PlayContext()
        var_0 = play_context_0.update_vars(dict_0)
        play_context_1 = module_0.PlayContext()
        var_1 = play_context_1.set_attributes_from_cli()
        var_2 = play_context_0.set_become_plugin(play_context_1)

if __name__ == "__main__":
    unittest.main()
