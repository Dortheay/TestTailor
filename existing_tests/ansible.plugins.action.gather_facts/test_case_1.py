import unittest
import timeout_decorator
import ansible.plugins.action.gather_facts

class Test_Gather_facts_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
