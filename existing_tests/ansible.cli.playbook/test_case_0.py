import unittest
import timeout_decorator
import ansible.cli.playbook as module_0

class Test_Playbook_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            playbook_c_l_i_0 = module_0.PlaybookCLI()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
