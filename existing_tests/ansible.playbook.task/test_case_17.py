import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 1168
            task_0 = module_0.Task(int_0)
            str_0 = 'eRi=07dI1"\x0c \'Q0!'
            bool_0 = False
            tuple_0 = (str_0, bool_0)
            list_0 = [task_0]
            bytes_0 = b'\x0e\x1b\xf3\xc5\xb6^ha\xdf\xee\xaa\x8eBtf\x1d\xe0\x10'
            var_0 = task_0.load(tuple_0, list_0, bytes_0, task_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
