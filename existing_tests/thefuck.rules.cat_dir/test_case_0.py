import unittest
import timeout_decorator
import thefuck.rules.cat_dir as module_0

class Test_Cat_dir_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'yuLZ9'
            var_0 = module_0.match(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
