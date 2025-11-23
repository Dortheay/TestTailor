import unittest
import timeout_decorator
import ansible.playbook.play_context as module_0

class Test_Play_context_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = 4922.81
            play_context_0 = module_0.PlayContext()
            var_0 = play_context_0.set_attributes_from_plugin(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
