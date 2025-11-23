import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0

class Test_Unsafe_proxy_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        bytes_0 = b'\x02n\xa7\xfcD\x15\xf1;\xa8\n'
        list_0 = []
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes(*list_0)
        var_0 = module_0.wrap_var(bytes_0)

if __name__ == "__main__":
    unittest.main()
