import unittest
import timeout_decorator
import httpie.cli.requestitems as module_0
import httpie.cli.argtypes as module_1

class Test_Requestitems_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        request_items_0 = module_0.RequestItems()

if __name__ == "__main__":
    unittest.main()
