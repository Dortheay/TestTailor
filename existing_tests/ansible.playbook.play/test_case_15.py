import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            play_0 = module_0.Play()
            play_1 = module_0.Play()
            var_0 = play_1.get_handlers()
            var_1 = play_1.copy()
            var_2 = play_0.serialize()
            var_3 = play_1.serialize()
            var_4 = play_1.get_handlers()
            int_0 = 318
            var_5 = play_0.preprocess_data(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
