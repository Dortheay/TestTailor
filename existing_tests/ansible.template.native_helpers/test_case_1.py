import unittest
import timeout_decorator
import ansible.template.native_helpers as module_0

class Test_Native_helpers_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b'J\x0e\xce\x13>\x0f\x84\xe9\xcfA@\xd4\xb8%'
        var_0 = module_0.ansible_native_concat(bytes_0)

if __name__ == "__main__":
    unittest.main()
