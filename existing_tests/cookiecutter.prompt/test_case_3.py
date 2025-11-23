import unittest
import timeout_decorator
import cookiecutter.prompt as module_0

class Test_Prompt_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'L 6*;\x0c%br)tx+=='
            str_1 = '<Dsl1ti!%%-?"j'
            set_0 = {str_0, str_1, str_0}
            var_0 = module_0.read_repo_password(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
