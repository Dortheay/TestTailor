import unittest
import timeout_decorator
import cookiecutter.repository as module_0

class Test_Repository_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bool_0 = False
            str_0 = 'm}\\Rby!og'
            int_0 = 2652
            list_0 = []
            bytes_0 = b'\xfb'
            var_0 = module_0.determine_repo_dir(bool_0, str_0, int_0, list_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
