import unittest
import timeout_decorator
import ansible.modules.pip as module_0

class Test_Pip_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '+L"8'
            float_0 = None
            dict_0 = {float_0: str_0, str_0: float_0}
            str_1 = 'us\x0cNG1;o%'
            package_0 = module_0.Package(dict_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
