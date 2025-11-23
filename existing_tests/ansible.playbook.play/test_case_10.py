import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            play_0 = module_0.Play()
            play_1 = module_0.Play()
            var_0 = play_1.compile()
            play_2 = module_0.Play()
            var_1 = play_1.get_tasks()
            dict_0 = {}
            var_2 = play_0.load(dict_0)
            var_3 = play_1.copy()
            float_0 = 2174.31
            var_4 = play_1.load(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
