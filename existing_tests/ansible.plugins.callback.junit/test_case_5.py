import unittest
import timeout_decorator
import ansible.plugins.callback.junit as module_0

class Test_Junit_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            int_0 = 4444
            set_0 = {bool_0}
            list_0 = [set_0, int_0, int_0, bool_0]
            tuple_0 = ()
            float_0 = -659.442
            tuple_1 = (list_0, tuple_0, float_0)
            bytes_0 = b'[\xa7E\xa1\x95\x1d\x8aGm\xa6-&\xdc\xabA<'
            str_0 = 's\rGdK-Y1kCu p_w>L'
            task_data_0 = module_0.TaskData(bytes_0, tuple_0, set_0, set_0, str_0)
            task_data_1 = module_0.TaskData(int_0, set_0, tuple_1, float_0, task_data_0)
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_playbook_on_start(task_data_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
