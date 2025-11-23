import unittest
import timeout_decorator
import youtube_dl.extractor.linuxacademy as module_0

class Test_Linuxacademy_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        linux_academy_i_e_0 = module_0.LinuxAcademyIE()

if __name__ == "__main__":
    unittest.main()
