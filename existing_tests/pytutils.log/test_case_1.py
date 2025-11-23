import unittest
import timeout_decorator
import pytutils.log as module_0

class Test_Log_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b"\n\x1c\xac\xceQ7\xa7,\x80A\x0e\xb1\xa6'[e"
            var_0 = module_0.configure(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
