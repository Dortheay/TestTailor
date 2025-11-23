import unittest
import timeout_decorator
import cookiecutter.repository as module_0

class Test_Repository_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'gh'
            str_1 = 'https://github.com/{0}'
            str_2 = {str_0: str_1}
            str_3 = '/tmp'
            str_4 = 'main'
            bool_0 = False
            var_0 = None
            var_1 = None
            var_2 = module_0.determine_repo_dir(str_3, str_2, str_3, str_4, bool_0, var_0, var_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
