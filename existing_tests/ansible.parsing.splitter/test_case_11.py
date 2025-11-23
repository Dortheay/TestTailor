import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bytes_0 = b"B\xb0\t'\xcb\xda|"
            var_0 = module_0.parse_kv(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
