import unittest
import timeout_decorator
import ansible.parsing.utils.jsonify as module_0

class Test_Jsonify_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'R[hf@vz'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        float_0 = -678.0
        tuple_0 = (str_0, dict_0, float_0)
        var_0 = module_0.jsonify(tuple_0, dict_0)

if __name__ == "__main__":
    unittest.main()
