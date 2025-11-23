import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        set_0 = set()
        distribution_0 = module_0.Distribution(set_0)
        bytes_0 = b'p1.#>\xd0\xe6\xf0\xf9Q'
        float_0 = 420.928
        str_0 = 'W=sJ7.Ta1l:\x0b'
        float_1 = 0.0
        tuple_0 = (str_0, float_1)
        distribution_1 = module_0.Distribution(tuple_0)
        distribution_files_0 = module_0.DistributionFiles(distribution_1)
        var_0 = distribution_files_0.parse_distribution_file_Alpine(distribution_0, bytes_0, float_0, distribution_0)

if __name__ == "__main__":
    unittest.main()
