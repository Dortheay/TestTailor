import unittest
import timeout_decorator
import ansible.template.native_helpers as module_0

class Test_Native_helpers_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bool_0 = False
        set_0 = {bool_0, bool_0}
        var_0 = module_0.ansible_native_concat(set_0)

if __name__ == "__main__":
    unittest.main()
