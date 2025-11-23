import unittest
import timeout_decorator
import thefuck.rules.dirty_unzip as module_0

class Test_Dirty_unzip_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\x05==\xa3\x07'
            var_0 = module_0.side_effect(bytes_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
