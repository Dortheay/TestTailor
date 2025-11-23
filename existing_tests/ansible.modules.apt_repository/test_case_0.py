import unittest
import timeout_decorator
import ansible.modules.apt_repository as module_0

class Test_Apt_repository_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = -2442.84815
            list_0 = [float_0, float_0]
            list_1 = None
            var_0 = module_0.install_python_apt(list_0, list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
