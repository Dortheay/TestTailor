import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = "Restore the original function to re.compile().\n\n    It is safe to call reset_compile() multiple times, it will always\n    restore re.compile() to the value that existed at import time.\n    Though the first call will reset back to the original (it doesn't\n    track nesting level)\n    "
            var_0 = module_0.lazy_import(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
