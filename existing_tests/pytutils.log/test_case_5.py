import unittest
import timeout_decorator
import pytutils.log as module_0

class Test_Log_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bytes_0 = b'\xfd'
            tuple_0 = (bytes_0,)
            var_0 = module_0.configure(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
