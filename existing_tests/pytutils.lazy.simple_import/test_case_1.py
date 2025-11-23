import unittest
import timeout_decorator
import pytutils.lazy.simple_import as module_0

class Test_Simple_import_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b';%l\xd9\xd5&U\xe6q\xa9+\x0f\xad\xf0\xeaUe\xe1='
        non_local_0 = module_0.NonLocal(bytes_0)

if __name__ == "__main__":
    unittest.main()
