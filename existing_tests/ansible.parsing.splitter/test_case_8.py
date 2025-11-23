import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = 60.0
            var_0 = module_0.parse_kv(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
