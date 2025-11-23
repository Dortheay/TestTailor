import unittest
import timeout_decorator
import ansible.cli.playbook as module_0

class Test_Playbook_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'fake_playbook.yml'
            playbook_c_l_i_0 = module_0.PlaybookCLI(str_0)
            var_0 = playbook_c_l_i_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
