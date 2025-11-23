import unittest
import timeout_decorator
import ansible.modules.pip as module_0

class Test_Pip_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bool_0 = False
            str_0 = 'utQ1l'
            set_0 = {str_0, str_0, str_0}
            package_0 = module_0.Package(set_0)
            list_0 = [package_0, package_0, str_0]
            package_1 = module_0.Package(list_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
