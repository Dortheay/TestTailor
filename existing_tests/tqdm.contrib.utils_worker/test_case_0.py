import unittest
import timeout_decorator
import tqdm.contrib.utils_worker as module_0

class Test_Utils_worker_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        mono_worker_0 = module_0.MonoWorker()

if __name__ == "__main__":
    unittest.main()
