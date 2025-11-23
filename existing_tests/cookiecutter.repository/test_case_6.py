import unittest
import timeout_decorator
import cookiecutter.repository as module_0

class Test_Repository_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'b4k"in\n52@n+m]6gffxe.zip'
            set_0 = set()
            float_0 = -494.242
            bytes_0 = b'\xb6\xa8\xbd!'
            list_0 = [float_0, bytes_0, str_0]
            var_0 = module_0.determine_repo_dir(str_0, set_0, float_0, bytes_0, set_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
