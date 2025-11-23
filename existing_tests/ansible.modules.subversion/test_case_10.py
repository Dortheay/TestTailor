import unittest
import timeout_decorator
import ansible.modules.subversion as module_0

class Test_Subversion_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            float_0 = -2697.71117
            list_0 = [float_0, float_0]
            bytes_0 = b'\x8b\x94\xa8\xb8'
            str_0 = 'atsible.modules.subversion'
            subversion_0 = module_0.Subversion(float_0, bytes_0, list_0, str_0, str_0, str_0, str_0, float_0)
            var_0 = subversion_0.get_revision()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
