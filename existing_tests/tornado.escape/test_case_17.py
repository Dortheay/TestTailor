import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = "nGDqwa`doPU^,'dh)"
        optional_0 = module_0.utf8(str_0)

if __name__ == "__main__":
    unittest.main()
