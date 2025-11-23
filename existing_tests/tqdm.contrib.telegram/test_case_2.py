import unittest
import timeout_decorator
import tqdm.contrib.telegram as module_0

class Test_Telegram_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b't\x19\x93\x9e$\x97\x99\x96\xaf'
            set_0 = None
            tuple_0 = (bytes_0, set_0, bytes_0)
            list_0 = [bytes_0, tuple_0, bytes_0, bytes_0]
            telegram_i_o_0 = module_0.TelegramIO(tuple_0, list_0)
            var_0 = telegram_i_o_0.write(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
