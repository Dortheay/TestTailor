import unittest
import timeout_decorator
import httpie.plugins.base as module_0

class Test_Base_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            formatter_plugin_0 = module_0.FormatterPlugin()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
