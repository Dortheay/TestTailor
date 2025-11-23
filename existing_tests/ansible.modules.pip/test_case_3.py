import unittest
import timeout_decorator
import ansible.modules.pip as module_0

class Test_Pip_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'example-pkg'
        str_1 = '1.0.0'
        package_0 = module_0.Package(str_0, str_1)
        var_0 = str(package_0)
        str_2 = 'another-pkg'
        package_1 = module_0.Package(str_2)
        var_1 = str(package_1)
        str_3 = 'complex-pkg-name_with.dots'
        str_4 = '2.0.0-alpha'
        package_2 = module_0.Package(str_3, str_4)
        var_2 = str(package_2)
        str_5 = 'invalid-pkg'
        str_6 = 'invalid-version'
        package_3 = module_0.Package(str_5, str_6)
        var_3 = str(package_3)

if __name__ == "__main__":
    unittest.main()
