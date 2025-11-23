import unittest
import timeout_decorator
import httpie.output.formatters.colors as module_0
import httpie.context as module_1

class Test_Colors_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        solarized256_style_0 = module_0.Solarized256Style()

if __name__ == "__main__":
    unittest.main()
