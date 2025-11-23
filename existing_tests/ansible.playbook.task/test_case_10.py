import unittest
import timeout_decorator
import ansible.playbook.task as module_0

class Test_Task_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        set_0 = None
        set_1 = None
        dict_0 = {set_0: set_0, set_0: set_0, set_0: set_0, set_0: set_1}
        float_0 = -965.06964
        bytes_0 = b'\xce\x16\xd6\x91\xc3J\x95\xcd\xb0\xa2\xda'
        task_0 = module_0.Task(float_0, bytes_0)
        var_0 = task_0.deserialize(dict_0)

if __name__ == "__main__":
    unittest.main()
