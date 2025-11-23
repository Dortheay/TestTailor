import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bytes_0 = b']\xa3\xf4\x97\x98 \xd7I`\xc01\xc6\x8fJ'
            set_0 = {bytes_0, bytes_0}
            var_0 = module_0.to_bytes(set_0)
            str_0 = None
            float_0 = 1576.06895
            list_0 = [str_0, set_0]
            tuple_0 = None
            var_1 = module_0.to_text(tuple_0, float_0)
            var_2 = module_0.container_to_bytes(list_0)
            float_1 = 735.71916
            var_3 = module_0.to_bytes(float_0, float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
