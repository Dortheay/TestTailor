import unittest
import timeout_decorator
import cookiecutter.repository as module_0

class Test_Repository_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '/mock/repo'
        var_0 = module_0.repository_has_cookiecutter_json(str_0)
        var_1 = module_0.repository_has_cookiecutter_json(str_0)

if __name__ == "__main__":
    unittest.main()
