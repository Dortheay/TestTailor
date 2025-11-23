import unittest
import timeout_decorator
import ansible.modules.apt_repository as module_0

class Test_Apt_repository_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        invalid_source_0 = module_0.InvalidSource()

if __name__ == "__main__":
    unittest.main()
