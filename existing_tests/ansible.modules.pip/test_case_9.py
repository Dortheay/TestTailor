import unittest
import timeout_decorator
import ansible.modules.pip as module_0

class Test_Pip_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'utQ1l'
            str_1 = 'U^15x68tN`O'
            package_0 = module_0.Package(str_1)
            var_0 = package_0.__str__()
            set_0 = {str_0, str_0, str_0}
            package_1 = module_0.Package(set_0)
            list_0 = [package_1, package_1, str_0]
            bool_0 = False
            package_2 = module_0.Package(list_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
