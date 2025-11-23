import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bool_0 = False
        distribution_files_0 = module_0.DistributionFiles(bool_0)

if __name__ == "__main__":
    unittest.main()
