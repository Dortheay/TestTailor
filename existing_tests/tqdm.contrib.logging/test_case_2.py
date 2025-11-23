import unittest
import timeout_decorator
import tqdm.contrib.logging as module_0
import logging as module_1

class Test_Logging_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        set_0 = set()
        tqdm_logging_handler_0 = module_0._TqdmLoggingHandler()
        var_0 = tqdm_logging_handler_0.emit(set_0)

if __name__ == "__main__":
    unittest.main()
