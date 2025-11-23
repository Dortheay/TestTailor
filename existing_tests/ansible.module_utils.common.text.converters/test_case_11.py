import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b'\xe8\xdbo\x08\xe0\xa3Z\xfb\xf7\x04\xc8E'
        var_0 = module_0.to_text(bytes_0)

if __name__ == "__main__":
    unittest.main()
