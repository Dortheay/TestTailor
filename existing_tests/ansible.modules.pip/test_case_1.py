import unittest
import timeout_decorator
import ansible.modules.pip as module_0

class Test_Pip_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '+L"8'
        package_0 = module_0.Package(str_0)

if __name__ == "__main__":
    unittest.main()
