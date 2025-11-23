import unittest
import timeout_decorator
import ansible.modules.pip as module_0

class Test_Pip_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            dict_0 = {}
            str_0 = 'J'
            package_0 = module_0.Package(str_0)
            var_0 = package_0.is_satisfied_by(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
