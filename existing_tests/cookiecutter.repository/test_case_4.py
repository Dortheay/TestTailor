import unittest
import timeout_decorator
import cookiecutter.repository as module_0

class Test_Repository_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            float_0 = -2239.0
            var_0 = module_0.repository_has_cookiecutter_json(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
