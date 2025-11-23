import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        float_0 = -2201.399
        int_0 = -1432090515
        str_0 = 'Y@Z'
        str_1 = "D[N%'^\x0bYo-'B Cy%\nh"
        dict_0 = {str_1: float_0, str_1: float_0}
        dict_1 = {}
        tuple_0 = (float_0, str_1, dict_0, dict_1)
        file_downloader_0 = module_0.FileDownloader(tuple_0, dict_0)
        var_0 = file_downloader_0.format_retries(int_0)
        var_1 = file_downloader_0.slow_down(dict_1, float_0, str_0)
        bool_0 = True
        list_0 = []
        list_1 = [list_0, list_0, list_0]
        list_2 = [var_1]
        file_downloader_1 = module_0.FileDownloader(list_1, list_2)
        bytes_0 = b'\xbeI_\xbe\xff<\xb9\xeb\n'
        int_1 = -489
        float_1 = 414.196175
        var_2 = file_downloader_1.calc_eta(int_0, int_1, bool_0, float_1)
        str_2 = '#!O.;AAANN|`j[~Y\x0b?.J'
        var_3 = file_downloader_0.try_utime(str_2, bytes_0)

if __name__ == "__main__":
    unittest.main()
