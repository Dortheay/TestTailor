import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        float_0 = 5845.04
        str_0 = 'gDO'
        str_1 = 'K<BgG\rz}<5=~=Y6\n'
        str_2 = "D[N%'^\x0bYo-'B Cy%\nh"
        float_1 = -362.546
        dict_0 = {str_1: float_0, str_2: float_1}
        dict_1 = {}
        tuple_0 = (float_1, str_1, dict_0, dict_1)
        file_downloader_0 = module_0.FileDownloader(tuple_0, dict_0)
        var_0 = file_downloader_0.slow_down(dict_1, float_0, str_0)
        list_0 = []
        var_1 = file_downloader_0.try_rename(list_0, list_0)

if __name__ == "__main__":
    unittest.main()
