import unittest
import timeout_decorator
import cookiecutter.repository as module_0

class Test_Repository_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bytes_0 = b'\xde\x15V<\xe2b;\xd0g\xcc\x1e\xa0\xaf\xd8\x8f'
            var_0 = module_0.repository_has_cookiecutter_json(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
