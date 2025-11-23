import unittest
import timeout_decorator
import cookiecutter.repository as module_0

class Test_Repository_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '~/.cookiecutters/'
            var_0 = {}
            str_1 = '!main'
            bool_0 = True
            var_1 = module_0.determine_repo_dir(str_0, var_0, str_0, str_1, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
