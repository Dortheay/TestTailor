import unittest
import timeout_decorator
import tqdm.contrib.telegram as module_0

class Test_Telegram_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '-|7&@6'
            str_1 = '2'
            telegram_i_o_0 = module_0.TelegramIO(str_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
