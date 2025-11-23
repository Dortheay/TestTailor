import unittest
import timeout_decorator
import tqdm.contrib.telegram as module_0

class Test_Telegram_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'ascii'
            str_1 = '}w'
            str_2 = '\n        Wrapper for `asyncio.as_completed`.\n        '
            dict_0 = {str_0: str_0, str_1: str_0, str_1: str_1, str_2: str_2}
            var_0 = module_0.ttgrange(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
