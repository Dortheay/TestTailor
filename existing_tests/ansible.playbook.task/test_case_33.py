import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = '0 t*'
            tuple_0 = (str_0,)
            int_0 = 512
            str_1 = '0Wzw3h\x0cra'
            str_2 = '\n6$k'
            bool_0 = True
            task_0 = module_0.Task(tuple_0, bool_0)
            var_0 = task_0.copy(str_2)
            bytes_0 = b'\xd4cU'
            bytes_1 = b'\xf3i\x9b\x86\x87\xd7 \xfdl'
            task_1 = module_0.Task(bytes_1)
            var_1 = task_1.load(int_0, str_1, str_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
