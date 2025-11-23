import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            int_0 = 604800
            complex_0 = None
            str_0 = '[Kk5*TZWZ~2:;x.'
            var_0 = module_0.container_to_bytes(complex_0, str_0)
            var_1 = module_0.to_text(int_0)
            set_0 = set()
            var_2 = module_0.jsonify(set_0)
            list_0 = []
            tuple_0 = (list_0,)
            list_1 = []
            var_3 = module_0.to_bytes(list_1, tuple_0, int_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
