import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            dict_0 = {}
            str_0 = '+Myz&<z$JM|\t>I'
            tuple_0 = (str_0, str_0)
            var_0 = module_0.container_to_bytes(dict_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
