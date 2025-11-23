import unittest
import timeout_decorator
import ansible.playbook.play_context as module_0

class Test_Play_context_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        play_context_0 = module_0.PlayContext()

if __name__ == "__main__":
    unittest.main()
