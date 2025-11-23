import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        dict_0 = {}
        play_0 = module_0.Play()
        var_0 = play_0.get_vars()
        var_1 = play_0.get_name()
        var_2 = play_0.get_name()
        play_1 = module_0.Play()
        var_3 = play_1.get_vars_files()
        play_2 = module_0.Play()
        var_4 = play_0.get_tasks()
        play_3 = module_0.Play()
        var_5 = play_1.deserialize(dict_0)
        var_6 = play_2.compile_roles_handlers()

if __name__ == "__main__":
    unittest.main()
