import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            float_0 = 2716.0
            set_0 = {float_0}
            str_0 = '+jf'
            list_0 = [str_0]
            import_replacer_0 = module_0.ImportReplacer(set_0, str_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
