import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        play_0 = module_0.Play()
        var_0 = play_0.serialize()

if __name__ == "__main__":
    unittest.main()
