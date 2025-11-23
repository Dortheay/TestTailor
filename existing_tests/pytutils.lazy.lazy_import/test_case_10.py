import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            list_0 = []
            str_0 = 'J?U]<bQ\x0c()gE'
            bytes_0 = b'\x9c\x0b\xb6\x15$\xdfC\x82{_/d~'
            import_processor_0 = module_0.ImportProcessor(bytes_0)
            var_0 = import_processor_0.lazy_import(list_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
