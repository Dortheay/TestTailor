import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b'\x00'
        dict_0 = {}
        var_0 = module_0.remove_values(bytes_0, dict_0)

if __name__ == "__main__":
    unittest.main()
