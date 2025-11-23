import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        set_0 = None
        var_0 = module_0.parse_kv(set_0)

if __name__ == "__main__":
    unittest.main()
