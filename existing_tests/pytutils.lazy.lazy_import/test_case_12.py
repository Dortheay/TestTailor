import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = '@\x0bw}MsiC:m\x0cm);#]f}'
            var_0 = module_0.lazy_import(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
