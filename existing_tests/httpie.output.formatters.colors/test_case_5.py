import unittest
import timeout_decorator
import httpie.context as module_0
import httpie.output.formatters.colors as module_1

class Test_Colors_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            environment_0 = module_0.Environment()
            color_formatter_0 = module_1.ColorFormatter(environment_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
