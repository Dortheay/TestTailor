import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b'\x1b\x87'
        distribution_0 = module_0.Distribution(bytes_0)
        var_0 = distribution_0.get_distribution_SMGL()
        var_1 = distribution_0.get_distribution_facts()

if __name__ == "__main__":
    unittest.main()
