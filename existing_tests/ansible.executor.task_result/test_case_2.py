import unittest
import timeout_decorator
import ansible.executor.task_result as module_0

class Test_Task_result_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'A)r>a|\t\x0cA)!\x0br*Ar'
        bool_0 = True
        list_0 = [bool_0]
        list_1 = [bool_0, bool_0, list_0, list_0]
        tuple_0 = ()
        tuple_1 = (bool_0, list_1, tuple_0)
        dict_0 = {}
        task_result_0 = module_0.TaskResult(str_0, tuple_1, dict_0)
        var_0 = task_result_0.is_failed()

if __name__ == "__main__":
    unittest.main()
