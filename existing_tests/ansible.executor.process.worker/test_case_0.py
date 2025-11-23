import unittest
import timeout_decorator
import ansible.executor.process.worker

class Test_Worker_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
