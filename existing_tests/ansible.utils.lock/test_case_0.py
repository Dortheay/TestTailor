import unittest
import timeout_decorator
import ansible.utils.lock as module_0

class Test_Lock_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.lock_decorator()

if __name__ == "__main__":
    unittest.main()
