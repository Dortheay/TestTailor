import unittest
import timeout_decorator
import ansible.modules.pip as module_0

class Test_Pip_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '+L"8'
        package_0 = module_0.Package(str_0)
        bytes_0 = b'[j\xd7\x8d\xd0\xa5_J'
        var_0 = package_0.is_satisfied_by(bytes_0)

if __name__ == "__main__":
    unittest.main()
