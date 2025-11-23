import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = -559.3194
            tuple_0 = None
            bytes_0 = b'\xd7<`\x19\x0e$\xd9\x9f\xb0'
            var_0 = module_0.to_text(tuple_0, bytes_0, tuple_0)
            bytes_1 = b'\xef3\x81\xf4p\xe9\xe5G'
            bool_0 = False
            int_0 = 1083
            var_1 = module_0.container_to_text(bool_0, int_0)
            var_2 = module_0.to_text(float_0, tuple_0, bytes_1, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
