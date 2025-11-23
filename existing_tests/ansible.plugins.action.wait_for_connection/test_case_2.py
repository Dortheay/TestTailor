import unittest
import timeout_decorator
import ansible.plugins.action.wait_for_connection as module_0

class Test_Wait_for_connection_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '#ML{NR'
            dict_0 = {str_0: str_0}
            int_0 = 1920
            list_0 = [dict_0, dict_0, dict_0, int_0]
            str_1 = ''
            timed_out_exception_0 = module_0.TimedOutException()
            str_2 = '\rF"XH'
            str_3 = 'jI.\t1<eba^A8\\9'
            action_module_0 = module_0.ActionModule(list_0, str_1, timed_out_exception_0, str_2, int_0, str_3)
            timed_out_exception_1 = module_0.TimedOutException()
            str_4 = '\n        Perform the action on an Ansible Galaxy role. Must be combined with a further action like delete/install/init\n        as listed below.\n        '
            float_0 = -2268.0
            set_0 = {timed_out_exception_1, timed_out_exception_1, float_0}
            action_module_1 = module_0.ActionModule(timed_out_exception_1, str_4, float_0, str_4, str_4, set_0)
            var_0 = action_module_1.do_until_success_or_timeout(dict_0, str_0, int_0, dict_0, action_module_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
