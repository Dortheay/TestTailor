import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        bytes_0 = b'\x0b\x8c'
        float_0 = 1.0
        list_0 = [bytes_0, bytes_0, bytes_0, float_0]
        str_0 = 'cloud-services'
        tuple_0 = (list_0, str_0)
        var_0 = module_0.jsonify(tuple_0)

if __name__ == "__main__":
    unittest.main()
