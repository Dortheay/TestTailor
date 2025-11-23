import unittest
import timeout_decorator
import cookiecutter.repository as module_0

class Test_Repository_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'gh'
            str_1 = {str_0: str_0}
            str_2 = '/tmp'
            str_3 = 'main'
            bool_0 = False
            var_0 = None
            var_1 = module_0.determine_repo_dir(str_2, str_1, str_2, str_3, bool_0, var_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
