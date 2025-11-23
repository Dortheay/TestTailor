import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0
import ansible.utils.native_jinja as module_1

class Test_Unsafe_proxy_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            ansible_unsafe_0 = module_0.AnsibleUnsafe()
            str_0 = "blp'K~>-}`xc}fO"
            dict_0 = {str_0: str_0}
            int_0 = -1753
            list_0 = [ansible_unsafe_0, dict_0, int_0]
            unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)
            list_1 = [ansible_unsafe_0]
            var_0 = module_0.to_unsafe_text(*list_1)
            unsafe_proxy_1 = module_0.UnsafeProxy()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
