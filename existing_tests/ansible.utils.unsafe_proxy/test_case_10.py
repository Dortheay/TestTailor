import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0

class Test_Unsafe_proxy_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        set_0 = set()
        var_0 = module_0.wrap_var(set_0)
        str_0 = '^V&r0}d0!h\x0cH^M'
        list_0 = [str_0]
        var_1 = module_0.to_unsafe_text(*list_0)
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText()
        tuple_0 = None
        var_2 = module_0.wrap_var(tuple_0)

if __name__ == "__main__":
    unittest.main()
