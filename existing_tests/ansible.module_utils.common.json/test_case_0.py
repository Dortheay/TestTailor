import unittest
import timeout_decorator
import ansible.module_utils.common.json as module_0

class Test_Json_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '07A;6'
            bytes_0 = b'{\x94\xd0\xe8\x89\x8e\xd0^z\x07K\xb8!\x9f\xaa'
            ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(str_0, bytes_0)
            str_1 = '7K_.p3;\x0ca^~>'
            dict_0 = {str_0: ansible_j_s_o_n_encoder_0, str_1: str_1}
            var_0 = ansible_j_s_o_n_encoder_0.iterencode(dict_0)
            ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
