import unittest
import timeout_decorator
import ansible.modules.pip as module_0

class Test_Pip_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'foo'
        str_1 = '1.0'
        package_0 = module_0.Package(str_0, str_1)
        str_2 = 'bar'
        package_1 = module_0.Package(str_2)
        str_3 = 'baz'
        str_4 = '2.0'
        package_2 = module_0.Package(str_3, str_4)
        str_5 = '1.0'
        str_6 = '2.0'
        var_0 = package_0.is_satisfied_by(str_5)
        var_1 = package_0.is_satisfied_by(str_6)
        var_2 = package_1.is_satisfied_by(str_5)
        var_3 = package_2.is_satisfied_by(str_5)

if __name__ == "__main__":
    unittest.main()
