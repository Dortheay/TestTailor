import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = -2852
            str_0 = '[{=Qe5\t2V\\'
            bytes_0 = b'5\x86\x1d\x17\xfa\x92\x13\xad'
            request_with_method_0 = module_0.RequestWithMethod(int_0, str_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
