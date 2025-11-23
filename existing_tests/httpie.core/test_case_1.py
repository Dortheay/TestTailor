import unittest
import timeout_decorator
import httpie.core as module_0
import httpie.context as module_1

class Test_Core_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        exit_status_0 = module_0.main()

if __name__ == "__main__":
    unittest.main()
