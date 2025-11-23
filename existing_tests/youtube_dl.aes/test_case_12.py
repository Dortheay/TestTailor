import unittest
import timeout_decorator
import youtube_dl.aes as module_0

class Test_Aes_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'VGYG9$wb`Dd< Hg^'
            float_0 = -2708.55
            var_0 = module_0.key_schedule_core(str_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
