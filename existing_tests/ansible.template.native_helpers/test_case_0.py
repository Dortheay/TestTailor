import unittest
import timeout_decorator
import ansible.template.native_helpers as module_0

class Test_Native_helpers_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        tuple_0 = ()
        var_0 = module_0.ansible_native_concat(tuple_0)

if __name__ == "__main__":
    unittest.main()
