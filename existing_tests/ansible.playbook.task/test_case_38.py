import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_39(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            task_0 = module_0.Task()
            str_0 = 'ansible.builtin'
            str_1 = [str_0]
            str_2 = 'vars'
            str_3 = 'collections'
            var_0 = task_0.serialize()
            str_4 = 'action'
            str_5 = 'key'
            var_1 = task_0.__repr__()
            str_6 = {str_5: str_5}
            var_2 = {str_2: str_6, str_3: str_1, str_4: str_3}
            var_3 = task_0.preprocess_data(var_2)
            var_4 = task_0.serialize()
            bytes_0 = b't\x11\xcd\xf9\xd4\x8c\x95\x92c#'
            dict_0 = {bytes_0: var_2, str_0: str_6}
            bytes_1 = b'\x80W%\xc3\xe2\xe3'
            var_5 = task_0.load(dict_0, bytes_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
