import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bytes_0 = b'Z\x0e\x0f\x90\x0cCl\xd9 \xe4\x08'
        var_0 = module_0.parse_kv(bytes_0)

if __name__ == "__main__":
    unittest.main()
