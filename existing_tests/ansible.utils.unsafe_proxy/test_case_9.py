import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0

class Test_Unsafe_proxy_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '^V&r0}d0!h\x0cH^M'
        list_0 = [str_0]
        var_0 = module_0.to_unsafe_text(*list_0)
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)

if __name__ == "__main__":
    unittest.main()
