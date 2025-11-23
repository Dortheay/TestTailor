import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            range_0 = module_0.Range()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
