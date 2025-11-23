import unittest
import timeout_decorator
import tqdm.contrib.telegram as module_0

class Test_Telegram_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = '\naoE-}B1PM(1Cq)RSH'
            dict_0 = {str_0: str_0}
            tqdm_telegram_0 = module_0.tqdm_telegram(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
