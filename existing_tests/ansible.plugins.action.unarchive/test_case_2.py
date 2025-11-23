import unittest
import timeout_decorator
import ansible.plugins.action.unarchive

class Test_Unarchive_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
