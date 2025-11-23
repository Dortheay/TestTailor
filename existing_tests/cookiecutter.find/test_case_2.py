import unittest
import timeout_decorator
import cookiecutter.find

class Test_Find_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
