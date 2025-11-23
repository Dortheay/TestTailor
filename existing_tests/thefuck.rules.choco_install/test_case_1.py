import unittest
import timeout_decorator
import thefuck.rules.choco_install as module_0

class Test_Choco_install_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = -744.22099
            var_0 = module_0.get_new_command(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
