import unittest
import timeout_decorator
import ansible.playbook.play_context as module_0

class Test_Play_context_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        play_context_0 = module_0.PlayContext()
        var_0 = play_context_0.set_attributes_from_cli()

if __name__ == "__main__":
    unittest.main()
