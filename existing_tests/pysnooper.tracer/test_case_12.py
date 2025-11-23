import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'path'
            list_0 = [str_0, str_0]
            str_1 = "FXkJ'SX,'Fr[E"
            tuple_0 = (list_0, str_1)
            file_writer_0 = module_0.FileWriter(str_0, tuple_0)
            tracer_0 = module_0.Tracer(file_writer_0)
            var_0 = tracer_0.__enter__()
            float_0 = 79.218764
            var_1 = tracer_0.__call__(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
