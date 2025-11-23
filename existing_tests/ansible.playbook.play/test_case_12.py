import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            play_0 = module_0.Play()
            var_0 = play_0.get_name()
            play_1 = module_0.Play()
            var_1 = play_1.get_vars()
            var_2 = play_1.serialize()
            var_3 = play_1.serialize()
            dict_0 = {}
            play_2 = module_0.Play()
            var_4 = play_1.load(play_0, play_1, dict_0, play_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
