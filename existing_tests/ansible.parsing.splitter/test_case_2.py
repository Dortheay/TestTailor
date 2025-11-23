import unittest
import timeout_decorator
import ansible.parsing.splitter as module_0

class Test_Splitter_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'C@=;).8=!v:,MG'
        var_0 = module_0.parse_kv(str_0)

if __name__ == "__main__":
    unittest.main()
