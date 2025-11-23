import unittest
import timeout_decorator
import tqdm.contrib.logging as module_0
import logging as module_1

class Test_Logging_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        var_0 = module_0.tqdm_logging_redirect()
        complex_0 = None
        str_0 = '8??SB|w5/0E}:mDJt'
        tqdm_logging_handler_0 = module_0._TqdmLoggingHandler()
        bool_0 = True
        set_0 = set()
        bytes_0 = b'\x97\x01\xfcz\xf6'
        list_0 = []
        float_0 = 0.3
        int_0 = None
        stream_handler_0 = None
        tuple_0 = (stream_handler_0,)
        str_1 = ';x3`g'
        dict_0 = {str_0: tuple_0, str_1: tqdm_logging_handler_0}
        log_record_0 = module_1.LogRecord(set_0, bytes_0, list_0, bool_0, float_0, int_0, tqdm_logging_handler_0, str_0, **dict_0)
        list_1 = []
        log_record_1 = module_1.LogRecord(bool_0, str_0, set_0, log_record_0, stream_handler_0, set_0, list_0, list_1)
        var_1 = tqdm_logging_handler_0.emit(log_record_1)
        float_1 = 1562.8979
        dict_1 = {str_0: str_0, str_0: float_1}
        var_2 = module_0.logging_redirect_tqdm()
        var_3 = module_0.tqdm_logging_redirect(**dict_1)
        int_1 = -2972
        var_4 = tqdm_logging_handler_0.emit(int_1)
        tqdm_logging_handler_1 = module_0._TqdmLoggingHandler(complex_0)
        var_5 = module_0.tqdm_logging_redirect()
        var_6 = tqdm_logging_handler_1.emit(dict_1)
        bytes_1 = b'r$\xc3?\x80\x88\x9c\x9f\x00\xe7~\xb2~$2t\xe94'
        var_7 = tqdm_logging_handler_1.emit(bytes_1)
        var_8 = module_0.tqdm_logging_redirect()

if __name__ == "__main__":
    unittest.main()
