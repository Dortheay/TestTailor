import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0
import ansible.utils.native_jinja as module_1

class Test_Unsafe_proxy_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText()
            ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
            dict_0 = {}
            list_0 = [native_jinja_unsafe_text_0, dict_0, ansible_unsafe_bytes_0]
            var_0 = module_0.to_unsafe_text(*list_0)
            ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
            var_1 = module_0.wrap_var(ansible_unsafe_text_0)
            list_1 = [native_jinja_unsafe_text_0, native_jinja_unsafe_text_0, native_jinja_unsafe_text_0, native_jinja_unsafe_text_0]
            dict_1 = {}
            ansible_unsafe_text_1 = module_0.AnsibleUnsafeText()
            var_2 = ansible_unsafe_text_1.encode(*list_1, **dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
