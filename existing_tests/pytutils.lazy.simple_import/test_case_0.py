import unittest
import timeout_decorator
import pytutils.lazy.simple_import as module_0

class Test_Simple_import_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        lazy_module_marker_0 = module_0._LazyModuleMarker()

if __name__ == "__main__":
    unittest.main()
