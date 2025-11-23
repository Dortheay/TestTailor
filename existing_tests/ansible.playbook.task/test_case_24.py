import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            bytes_0 = b'\xdd\xed\xe7\x0e\xe4\xb7\xfbI\x05\xe0\xd8\xcd\xa1\xf1\xff|j'
            list_0 = []
            task_0 = module_0.Task(bytes_0, list_0)
            var_0 = task_0.serialize()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
