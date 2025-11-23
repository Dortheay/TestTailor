import unittest
import timeout_decorator
import ansible.modules.pip as module_0

class Test_Pip_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            dict_0 = None
            str_0 = '+L"8'
            package_0 = module_0.Package(str_0)
            var_0 = package_0.canonicalize_name(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
