import unittest
import timeout_decorator
import ansible.plugins.become.su as module_0

class Test_Su_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        become_module_0 = module_0.BecomeModule()

if __name__ == "__main__":
    unittest.main()
