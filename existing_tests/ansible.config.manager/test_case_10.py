import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'p4\x0b)q'
            str_1 = '\nuser_input:\n  description: User input from interactive console\n  returned: if no waiting time set\n  type: str\n  sample: Example user input\nstart:\n  description: Time when started pausing\n  returned: always\n  type: str\n  sample: "2017-02-23 14:35:07.298862"\nstop:\n  description: Time when ended pausing\n  returned: always\n  type: str\n  sample: "2017-02-23 14:35:09.552594"\ndelta:\n  description: Time paused in seconds\n  returned: always\n  type: str\n  sample: 2\nstdout:\n  description: Output of pause module\n  returned: always\n  type: str\n  sample: Paused for 0.04 minutes\necho:\n  description: Value of echo setting\n  returned: always\n  type: bool\n  sample: true\n'
            str_2 = None
            dict_0 = {str_0: str_0, str_1: str_0, str_2: str_1, str_2: str_1}
            config_manager_0 = module_0.ConfigManager()
            var_0 = config_manager_0.update_config_data(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
