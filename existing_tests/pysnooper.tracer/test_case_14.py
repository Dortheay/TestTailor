import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = '<DSM3l.}|#\n;E.A'
            list_0 = [str_0, str_0]
            str_1 = "FXkJ'SX,'Fr[E"
            tuple_0 = (list_0, str_1)
            file_writer_0 = module_0.FileWriter(str_1, tuple_0)
            tracer_0 = module_0.Tracer(file_writer_0)
            var_0 = tracer_0.__enter__()
            file_writer_1 = module_0.FileWriter(str_1, list_0)
            var_1 = file_writer_1.write(str_0)
            bytes_0 = b't\x0c\xbd\x80\x86\xeeK'
            bool_0 = None
            var_2 = tracer_0.__exit__(bytes_0, tuple_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
