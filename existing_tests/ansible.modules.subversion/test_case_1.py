import unittest
import timeout_decorator
import ansible.modules.subversion as module_0

class Test_Subversion_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = -2697.71117
        list_0 = [float_0, float_0]
        bytes_0 = b'\xc1\x8f\xdfA?x\x01\x90^\x7f\xf3\xd1'
        str_0 = '_`mainW_'
        subversion_0 = module_0.Subversion(float_0, bytes_0, list_0, bytes_0, str_0, str_0, str_0, str_0)

if __name__ == "__main__":
    unittest.main()
