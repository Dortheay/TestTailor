import unittest
import timeout_decorator
import ansible.playbook.play_context as module_0

class Test_Play_context_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'V&d0o\t[&|P4;'
            play_context_0 = module_0.PlayContext(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
