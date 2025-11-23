import unittest
import timeout_decorator
import ansible.plugins.callback.junit as module_0

class Test_Junit_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            tuple_0 = ()
            list_0 = []
            float_0 = 881.0
            str_0 = '2'
            host_data_0 = module_0.HostData(tuple_0, list_0, float_0, str_0)
            callback_module_0 = module_0.CallbackModule()
            str_1 = '\'6t:>S+n(t.\ng6+Y"\r}'
            float_1 = 84.36867
            list_1 = [callback_module_0]
            bool_0 = False
            dict_0 = {callback_module_0: callback_module_0, bool_0: bool_0, bool_0: callback_module_0, float_1: list_1}
            set_0 = set()
            task_data_0 = module_0.TaskData(float_1, list_1, bool_0, dict_0, set_0)
            host_data_1 = module_0.HostData(float_1, list_1, task_data_0, callback_module_0)
            bytes_0 = b'\xf6>\xde\x8a\x8f\xdd\xd4\x13\x8d\xca\xdd\xc3\x0b\xc7`\x9e\xf1j-\x91'
            task_data_1 = module_0.TaskData(callback_module_0, str_1, host_data_1, bytes_0, str_1)
            var_0 = task_data_1.add_host(host_data_0)
            float_2 = None
            callback_module_1 = module_0.CallbackModule()
            var_1 = callback_module_1.v2_playbook_on_cleanup_task_start(float_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
