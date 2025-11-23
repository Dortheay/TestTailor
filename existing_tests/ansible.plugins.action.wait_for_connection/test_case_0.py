import unittest
import timeout_decorator
import ansible.plugins.action.wait_for_connection as module_0

class Test_Wait_for_connection_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = 2980.97985
            timed_out_exception_0 = module_0.TimedOutException()
            float_1 = 3416.8976
            str_0 = 'guJ\nu iZiue%w'
            list_0 = [float_1, float_0]
            set_0 = {float_1}
            list_1 = []
            dict_0 = {str_0: str_0}
            bytes_0 = b'\xd3(\xba\xea\x86\xf8OB=^\x11'
            list_2 = []
            bytes_1 = b'!\xe1\xf0R'
            float_2 = 1653.2
            action_module_0 = module_0.ActionModule(list_1, dict_0, bytes_0, list_2, bytes_1, float_2)
            bytes_2 = b'H\xc2\x12d\x18\x84\x13#\xb7\x93\xb4\xb0'
            set_1 = {bytes_2, bytes_2}
            str_1 = 'username'
            dict_1 = {str_1: set_1}
            timed_out_exception_1 = module_0.TimedOutException()
            action_module_1 = module_0.ActionModule(bytes_2, set_1, set_1, dict_1, bytes_2, timed_out_exception_1)
            var_0 = action_module_1.do_until_success_or_timeout(float_0, float_1, str_0, list_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
