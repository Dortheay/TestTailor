import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0
import ansible.utils.native_jinja as module_1

class Test_Unsafe_proxy_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '^V&r0}d0!h\x0cH^M'
            list_0 = [str_0]
            var_0 = module_0.to_unsafe_text(*list_0)
            float_0 = -1285.3721
            set_0 = {var_0}
            var_1 = module_0.wrap_var(set_0)
            str_1 = 'h]7WnJAw`&8=-gXyO&'
            dict_0 = {str_1: var_1, str_0: float_0, str_0: str_1, str_0: str_0}
            var_2 = module_0.to_unsafe_text(*list_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
