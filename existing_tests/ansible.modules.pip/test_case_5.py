import unittest
import timeout_decorator
import ansible.modules.pip as module_0

class Test_Pip_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'A+p"qM_f@FJ.l-`'
            package_0 = module_0.Package(str_0)
            float_0 = -4169.34239
            str_1 = "@5lvY'FE#1A&r<=,"
            bytes_0 = b'\xd5_\xf9'
            str_2 = 'MS46\td'
            var_0 = module_0.setup_virtualenv(float_0, package_0, str_1, bytes_0, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
