import unittest
import timeout_decorator
import ansible.playbook.conditional as module_0

class Test_Conditional_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            conditional_0 = module_0.Conditional()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
