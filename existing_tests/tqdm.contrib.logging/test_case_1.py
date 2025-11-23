import unittest
import timeout_decorator
import tqdm.contrib.logging as module_0
import logging as module_1

class Test_Logging_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        tqdm_logging_handler_0 = module_0._TqdmLoggingHandler()

if __name__ == "__main__":
    unittest.main()
