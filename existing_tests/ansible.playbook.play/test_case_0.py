import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        play_0 = module_0.Play()

if __name__ == "__main__":
    unittest.main()
