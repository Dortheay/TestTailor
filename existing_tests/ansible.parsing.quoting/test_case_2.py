import unittest
import timeout_decorator
import ansible.parsing.quoting as module_0

class Test_Quoting_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = None
        tuple_0 = (int_0,)
        var_0 = module_0.is_quoted(tuple_0)

if __name__ == "__main__":
    unittest.main()
