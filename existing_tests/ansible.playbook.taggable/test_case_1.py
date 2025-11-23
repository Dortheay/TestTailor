import unittest
import timeout_decorator
import ansible.playbook.taggable as module_0

class Test_Taggable_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        taggable_0 = module_0.Taggable()

if __name__ == "__main__":
    unittest.main()
