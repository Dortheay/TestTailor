import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0
import ansible.utils.native_jinja as module_1

class Test_Unsafe_proxy_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            var_0 = module_0.to_unsafe_bytes()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
