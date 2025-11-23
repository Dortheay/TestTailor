import unittest
import timeout_decorator
import ansible.executor.playbook_executor as module_0

class Test_Playbook_executor_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = -759.869
        tuple_0 = (float_0,)
        bool_0 = False
        bool_1 = False
        playbook_executor_0 = module_0.PlaybookExecutor(tuple_0, bool_0, bool_0, bool_1, bool_1)

if __name__ == "__main__":
    unittest.main()
