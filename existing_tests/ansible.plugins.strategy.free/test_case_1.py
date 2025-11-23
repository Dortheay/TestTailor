import unittest
import timeout_decorator
import ansible.plugins.strategy.free

class Test_Free_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
