import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'4\x1b\xce\xf6\x9a\xcb\x94'
            str_0 = 'Y2YKIV5'
            dict_0 = {str_0: bytes_0}
            str_1 = 'RGf\x0bYkh u7'
            var_0 = module_0.container_to_bytes(dict_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
