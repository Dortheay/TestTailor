import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_71(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        int_0 = 3186
        bytes_0 = b'\xae\x1f\x0cA9\xad\x1d\xa7'
        bytes_1 = b'\x07Kx\x9b\x9dSxW6`-$\xeb\x0b\xd6\x11\xa6\x8c'
        var_0 = module_0.ternary(bytes_0, bytes_1, int_0)

if __name__ == "__main__":
    unittest.main()
