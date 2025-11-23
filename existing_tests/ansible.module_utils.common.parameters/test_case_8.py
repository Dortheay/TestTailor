import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = 'tFB"jU00p>}RXD62'
        var_0 = module_0.remove_values(str_0, str_0)
        str_1 = 'n7y#$kpQ L>#%(\x0bR'
        str_2 = 'previous_boot_time'
        dict_0 = {str_2: str_1}
        bytes_0 = b'<\xad\x00\xb3\t\xf1\x93\r;\xa7\xb1\r\xac\xce\x89'
        tuple_0 = (dict_0, bytes_0, dict_0)
        list_0 = []
        var_1 = module_0.sanitize_keys(tuple_0, list_0)

if __name__ == "__main__":
    unittest.main()
