import unittest
import timeout_decorator
import pysnooper.tracer as module_0

class Test_Tracer_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '<DSM3l.}|#\n;E.A'
        str_1 = 'path'
        list_0 = [str_1, str_1]
        file_writer_0 = module_0.FileWriter(str_1, list_0)
        var_0 = file_writer_0.write(str_0)

if __name__ == "__main__":
    unittest.main()
