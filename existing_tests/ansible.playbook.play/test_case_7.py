import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        play_0 = module_0.Play()
        var_0 = play_0.copy()
        play_1 = module_0.Play()
        var_1 = play_0.get_tasks()

if __name__ == "__main__":
    unittest.main()
