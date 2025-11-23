import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0
import ansible.utils.native_jinja as module_1

class Test_Unsafe_proxy_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = '^V&r0}d0!h\x0cH^M'
            list_0 = [str_0]
            var_0 = module_0.to_unsafe_text(*list_0)
            list_1 = [list_0]
            str_1 = ''
            dict_0 = {str_1: list_1, str_0: list_1, str_1: str_0, str_1: str_0}
            unsafe_proxy_0 = module_0.UnsafeProxy(*list_1, **dict_0)
            native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
