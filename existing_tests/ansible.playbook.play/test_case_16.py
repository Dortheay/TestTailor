import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            play_0 = module_0.Play()
            var_0 = play_0.get_name()
            play_1 = module_0.Play()
            var_1 = play_1.serialize()
            var_2 = play_1.compile()
            bool_0 = False
            var_3 = play_1.deserialize(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
