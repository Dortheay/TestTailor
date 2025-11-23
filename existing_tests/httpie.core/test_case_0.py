import unittest
import timeout_decorator
import httpie.core as module_0
import httpie.context as module_1

class Test_Core_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
