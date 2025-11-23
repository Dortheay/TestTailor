import unittest
import timeout_decorator
import cookiecutter.repository as module_0

class Test_Repository_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'Lvxb\x0br$= X%#b#hmW'
        var_0 = module_0.is_repo_url(str_0)

if __name__ == "__main__":
    unittest.main()
