import unittest
import timeout_decorator
import httpie.context as module_0

class Test_Context_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            environment_0 = module_0.Environment()
            bool_0 = True
            bytes_0 = b'\x10\x8c\xba/\xa4\x01\xb3\x07'
            var_0 = environment_0.log_error(bool_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
