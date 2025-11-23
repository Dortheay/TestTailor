import unittest
import timeout_decorator
import ansible.playbook.play_context as module_0

class Test_Play_context_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            play_context_0 = module_0.PlayContext()
            play_context_1 = module_0.PlayContext()
            var_0 = play_context_1.update_vars(play_context_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
