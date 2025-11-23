import unittest
import timeout_decorator
import ansible.parsing.quoting as module_0

class Test_Quoting_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'starting to advance hosts'
        var_0 = module_0.unquote(str_0)

if __name__ == "__main__":
    unittest.main()
