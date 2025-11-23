import unittest
import timeout_decorator
import flutils.codecs.b64 as module_0

class Test_B64_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        module_0.register()

if __name__ == "__main__":
    unittest.main()
