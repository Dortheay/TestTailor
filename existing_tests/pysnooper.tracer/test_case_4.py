import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '<DSM3l.}|#\n;E.A'
        str_1 = 'path'
        list_0 = [str_1, str_1]
        str_2 = "FXkJ'SX,'Fr[E"
        tuple_0 = (list_0, str_2)
        file_writer_0 = module_0.FileWriter(str_1, tuple_0)
        tracer_0 = module_0.Tracer(file_writer_0)
        var_0 = tracer_0.__enter__()
        file_writer_1 = module_0.FileWriter(str_1, list_0)
        var_1 = file_writer_1.write(str_0)

if __name__ == "__main__":
    unittest.main()
