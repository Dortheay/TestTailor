import unittest
import timeout_decorator
import ansible.parsing.utils.jsonify as module_0

class Test_Jsonify_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 't\t'
            int_0 = None
            var_0 = module_0.jsonify(int_0)
            str_1 = 'NY" !ZrS\x0c/4z%d:er'
            var_1 = module_0.jsonify(str_1)
            var_2 = module_0.jsonify(str_0)
            float_0 = -1757.098
            var_3 = module_0.jsonify(float_0)
            bytes_0 = b'1\x8a\x94\xa3'
            float_1 = -1533.91489
            var_4 = module_0.jsonify(float_1, str_0)
            int_1 = -1461
            var_5 = module_0.jsonify(int_1)
            var_6 = module_0.jsonify(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
