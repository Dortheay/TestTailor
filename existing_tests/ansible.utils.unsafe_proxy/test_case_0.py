import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0
import ansible.utils.native_jinja as module_1

class Test_Unsafe_proxy_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 232
            list_0 = [int_0, int_0]
            dict_0 = {}
            ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
            var_0 = ansible_unsafe_bytes_0.decode(*list_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
