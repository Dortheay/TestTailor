import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '<DSM3l.}|#\n;E.A'
            list_0 = [str_0, str_0]
            str_1 = "FXkJ'SX,'Fr[E"
            tuple_0 = (list_0, str_1)
            file_writer_0 = module_0.FileWriter(str_1, tuple_0)
            tracer_0 = module_0.Tracer(file_writer_0)
            var_0 = tracer_0.__enter__()
            var_1 = tracer_0.__enter__()
            list_1 = None
            unavailable_source_0 = module_0.UnavailableSource(*list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
