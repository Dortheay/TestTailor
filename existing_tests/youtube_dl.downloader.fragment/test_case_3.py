import unittest
import timeout_decorator
import youtube_dl.downloader.fragment as module_0

class Test_Fragment_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'DMAar~d\ns,zRMSatf!_'
        str_1 = '\x0ciu[rk\x0b*y=F'
        float_0 = -3801.42035
        str_2 = 'zha'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: float_0, str_2: float_0}
        list_0 = [dict_0, str_1]
        list_1 = [list_0]
        bool_0 = False
        list_2 = [bool_0, bool_0, bool_0]
        http_quiet_downloader_0 = module_0.HttpQuietDownloader(bool_0, list_2)
        var_0 = http_quiet_downloader_0.to_screen(*list_1)

if __name__ == "__main__":
    unittest.main()
