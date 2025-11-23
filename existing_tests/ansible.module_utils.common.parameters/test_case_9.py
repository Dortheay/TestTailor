import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = 'tFB"jU00p>}RXD62'
        var_0 = module_0.remove_values(str_0, str_0)
        set_0 = set()
        str_1 = 'Oon/)j\rjX2}=29K6wSz'
        bytes_0 = b"\x08\x87e\xbf\xd1\xe8\x9f\xff\xac\x83'\x1d\x9a\xc8\x8d{\xd8"
        var_1 = module_0.sanitize_keys(set_0, str_1, bytes_0)

if __name__ == "__main__":
    unittest.main()
