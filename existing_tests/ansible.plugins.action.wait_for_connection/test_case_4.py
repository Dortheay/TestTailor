import unittest
import timeout_decorator
import ansible.plugins.action.wait_for_connection as module_0

class Test_Wait_for_connection_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '&y7#I\t7$'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
            bool_0 = True
            int_0 = 1815
            dict_1 = None
            list_0 = [dict_1, bool_0, str_0]
            bytes_0 = b'\xc5Q\xc9\xd9\xc1\x0f\xf5\x81'
            bool_1 = False
            list_1 = []
            action_module_0 = None
            action_module_1 = module_0.ActionModule(bool_1, int_0, dict_0, list_1, action_module_0, dict_0)
            float_0 = -1857.828991
            action_module_2 = module_0.ActionModule(action_module_1, bytes_0, float_0, float_0, list_1, action_module_0)
            float_1 = 0.001
            dict_2 = {}
            str_1 = 'failed to retrieve selinux context'
            action_module_3 = module_0.ActionModule(float_1, list_0, bool_0, dict_2, str_1, list_0)
            var_0 = action_module_3.run(action_module_2, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
