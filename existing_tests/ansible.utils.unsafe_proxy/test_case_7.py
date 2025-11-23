import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0
import ansible.utils.native_jinja as module_1

class Test_Unsafe_proxy_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'value2'
            bytes_0 = b'binary data'
            native_jinja_text_0 = module_1.NativeJinjaText()
            var_0 = module_0.wrap_var(native_jinja_text_0)
            str_1 = 'iu\\p#!)zGh8kB'
            str_2 = 'sles'
            str_3 = 'ce;`7)x<fqz&[ZS#!'
            set_0 = set()
            dict_0 = {str_1: str_0, str_2: bytes_0, str_3: set_0, str_2: str_1}
            unsafe_proxy_0 = module_0.UnsafeProxy(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
