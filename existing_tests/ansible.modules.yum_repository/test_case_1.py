import unittest
import timeout_decorator
import ansible.modules.yum_repository as module_0

class Test_Yum_repository_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.main()

if __name__ == "__main__":
    unittest.main()
