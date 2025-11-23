import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0

class Test_Unsafe_proxy_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = '^V&r0}d0!h\x0cH^M'
        native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText()
        list_0 = [str_0]
        float_0 = -1285.3721
        var_0 = module_0.wrap_var(float_0)
        var_1 = module_0.to_unsafe_text(*list_0)
        int_0 = 0
        dict_0 = {str_0: int_0, int_0: list_0}
        var_2 = module_0.wrap_var(dict_0)
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)

if __name__ == "__main__":
    unittest.main()
