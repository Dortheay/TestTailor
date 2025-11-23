import unittest
import timeout_decorator
import ansible.modules.subversion as module_0

class Test_Subversion_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            float_0 = -2697.71117
            list_0 = [float_0, float_0, float_0, float_0]
            bytes_0 = b'`\xd7'
            str_0 = 'ansible.modules.subversion'
            subversion_0 = module_0.Subversion(float_0, bytes_0, list_0, bytes_0, str_0, str_0, str_0, str_0)
            int_0 = -2406
            var_0 = subversion_0.export(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
