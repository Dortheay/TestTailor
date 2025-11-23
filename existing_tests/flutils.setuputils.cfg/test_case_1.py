import unittest
import timeout_decorator
import flutils.setuputils.cfg as module_0

class Test_Cfg_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '/fake_dir'
            generator_0 = module_0.each_sub_command_config(str_0)
            var_0 = list(generator_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
