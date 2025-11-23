import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            play_0 = module_0.Play()
            var_0 = play_0.get_roles()
            set_0 = set()
            play_1 = module_0.Play()
            var_1 = play_1.preprocess_data(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
