import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        import_processor_0 = module_0.ImportProcessor()

if __name__ == "__main__":
    unittest.main()
