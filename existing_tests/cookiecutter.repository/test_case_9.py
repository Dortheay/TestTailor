import unittest
import timeout_decorator
import cookiecutter.repository as module_0

class Test_Repository_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = 'kjb\x0bs+*wrQpoZs>q'
            str_1 = {str_0: str_0}
            str_2 = 'tmp'
            bool_0 = False
            var_0 = None
            var_1 = module_0.determine_repo_dir(str_2, str_1, str_2, str_1, bool_0, var_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
