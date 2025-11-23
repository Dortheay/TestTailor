import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            bytes_0 = b'4\x1b\xce\xf6\x9a\xcb\x94'
            str_0 = 'Y2YKIV5'
            dict_0 = {str_0: str_0, str_0: bytes_0, str_0: str_0, bytes_0: bytes_0}
            str_1 = 'subotions'
            bool_0 = False
            var_0 = module_0.to_text(bool_0, bool_0)
            bytes_1 = b'<U'
            var_1 = module_0.to_bytes(bytes_1, str_1)
            var_2 = module_0.jsonify(dict_0)
            dict_1 = {str_0: bytes_0}
            var_3 = module_0.container_to_bytes(dict_1, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
