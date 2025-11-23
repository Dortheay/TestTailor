import unittest
import timeout_decorator
import tqdm.contrib.utils_worker as module_0

class Test_Utils_worker_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bool_0 = True
        mono_worker_0 = module_0.MonoWorker()
        var_0 = mono_worker_0.submit(bool_0)
        mono_worker_1 = module_0.MonoWorker()

if __name__ == "__main__":
    unittest.main()
