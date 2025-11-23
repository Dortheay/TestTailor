import unittest
import timeout_decorator
import ansible.plugins.action.wait_for_connection as module_0

class Test_Wait_for_connection_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            dict_0 = {}
            list_0 = [dict_0, dict_0, dict_0, dict_0]
            int_0 = 9
            timed_out_exception_0 = module_0.TimedOutException()
            bytes_0 = b"\xda'l\xe3\xeb"
            action_module_0 = module_0.ActionModule(dict_0, dict_0, list_0, int_0, timed_out_exception_0, bytes_0)
            var_0 = action_module_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
