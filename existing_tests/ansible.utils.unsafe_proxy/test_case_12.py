import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0

class Test_Unsafe_proxy_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        float_0 = -1285.0
        var_0 = module_0.wrap_var(float_0)

if __name__ == "__main__":
    unittest.main()
