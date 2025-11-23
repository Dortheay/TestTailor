import unittest
import timeout_decorator
import thefuck.rules.dirty_unzip as module_0

class Test_Dirty_unzip_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = ';Rzze;},nJU[F'
            var_0 = module_0.get_new_command(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
