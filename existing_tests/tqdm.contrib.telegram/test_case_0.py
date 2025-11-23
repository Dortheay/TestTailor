import unittest
import timeout_decorator
import tqdm.contrib.telegram as module_0

class Test_Telegram_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            list_0 = None
            tqdm_telegram_0 = module_0.tqdm_telegram(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
