import unittest
import timeout_decorator
import ansible.utils.singleton

class Test_Singleton_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
