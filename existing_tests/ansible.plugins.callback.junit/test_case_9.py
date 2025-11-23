import unittest
import timeout_decorator
import ansible.plugins.callback.junit as module_0

class Test_Junit_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            complex_0 = None
            bytes_0 = b'\x1f<\x97\x9b'
            str_0 = ''
            float_0 = 3307.10355
            list_0 = [complex_0, float_0, float_0]
            set_0 = {complex_0}
            task_data_0 = module_0.TaskData(bytes_0, complex_0, float_0, list_0, set_0)
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_playbook_on_handler_task_start(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
