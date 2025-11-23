import unittest
import timeout_decorator
import ansible.plugins.action.service as module_0

class Test_Service_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'min_os_version'
            str_1 = '?s/*H\\7|o;0\rr}AH,dIR'
            dict_0 = {str_0: str_0, str_1: str_1, str_0: str_0, str_0: str_0}
            int_0 = -662
            str_2 = 'u^:>aKl0T'
            bytes_0 = b'ZY$\x8b\\Q\xbb\x86\xadj\x1f\xa06'
            str_3 = '\\PXQOU+h$n'
            action_module_0 = module_0.ActionModule(str_0, dict_0, int_0, str_2, bytes_0, str_3)
            var_0 = action_module_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
