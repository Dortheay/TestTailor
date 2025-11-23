import unittest
import timeout_decorator
import ansible.vars.reserved as module_0

class Test_Reserved_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        set_0 = set()
        var_0 = module_0.get_reserved_names(set_0)

if __name__ == "__main__":
    unittest.main()
