import unittest
import timeout_decorator
import ansible.module_utils.facts.utils as module_0

class Test_Utils_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bytes_0 = b'g\xc6\xd2e\xf5Ea!#|\xe67\x05\x8f\xcc\x8a'
        var_0 = module_0.get_file_lines(bytes_0)

if __name__ == "__main__":
    unittest.main()
