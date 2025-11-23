import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        play_0 = module_0.Play()
        var_0 = play_0.get_vars_files()

if __name__ == "__main__":
    unittest.main()
