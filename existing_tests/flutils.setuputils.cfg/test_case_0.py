import unittest
import timeout_decorator
import flutils.setuputils.cfg as module_0

class Test_Cfg_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            setup_cfg_command_config_0 = module_0.SetupCfgCommandConfig()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
