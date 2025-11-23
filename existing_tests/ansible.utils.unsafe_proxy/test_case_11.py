import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0

class Test_Unsafe_proxy_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bool_0 = False
        list_0 = [bool_0]
        var_0 = module_0.to_unsafe_text(*list_0)

if __name__ == "__main__":
    unittest.main()
