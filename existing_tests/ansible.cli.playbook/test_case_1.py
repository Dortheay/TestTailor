import unittest
import timeout_decorator
import ansible.cli.playbook as module_0

class Test_Playbook_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = 60.0
            playbook_c_l_i_0 = module_0.PlaybookCLI(float_0)
            var_0 = playbook_c_l_i_0.init_parser()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
