import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = '('
        dict_0 = {str_0: str_0}
        var_0 = module_0.jsonify(dict_0)

if __name__ == "__main__":
    unittest.main()
