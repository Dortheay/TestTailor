import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            play_0 = module_0.Play()
            var_0 = play_0.get_vars()
            var_1 = play_0.get_tasks()
            play_1 = module_0.Play()
            var_2 = play_1.copy()
            set_0 = set()
            var_3 = play_1.preprocess_data(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
