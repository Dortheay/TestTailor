import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        play_0 = module_0.Play()
        var_0 = play_0.compile_roles_handlers()

if __name__ == "__main__":
    unittest.main()
