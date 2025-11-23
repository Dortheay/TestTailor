import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = '\'J:l"E?qv+oB%qWDNNC'
            var_0 = module_0.parse_kv(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
