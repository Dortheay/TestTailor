import unittest
import timeout_decorator
import ansible.executor.process.worker as module_0

class Test_Worker_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            str_0 = "Cp!zU\r0l'"
            list_0 = [bool_0, bool_0, bool_0, str_0]
            tuple_0 = None
            str_1 = '<F'
            worker_process_0 = module_0.WorkerProcess(list_0, tuple_0, str_1, str_1, list_0, str_1, bool_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
