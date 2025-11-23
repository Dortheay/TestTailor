import unittest
import timeout_decorator
import tqdm.contrib.utils_worker as module_0

class Test_Utils_worker_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'V%4'
        list_0 = [str_0]
        mono_worker_0 = module_0.MonoWorker()
        dict_0 = {str_0: list_0}
        var_0 = mono_worker_0.submit(str_0, **dict_0)
        var_1 = mono_worker_0.submit(list_0)
        var_2 = mono_worker_0.submit(mono_worker_0, **dict_0)
        mono_worker_1 = module_0.MonoWorker()
        var_3 = mono_worker_0.submit(str_0)

if __name__ == "__main__":
    unittest.main()
