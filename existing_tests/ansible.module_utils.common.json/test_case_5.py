import unittest
import timeout_decorator
import ansible.module_utils.common.json as module_0

class Test_Json_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'HqauvuvWXZ<P\r'
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
        var_0 = ansible_j_s_o_n_encoder_0.iterencode(str_0)
        int_0 = 167
        ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder()
        var_1 = ansible_j_s_o_n_encoder_1.iterencode(int_0)
        int_1 = 117
        ansible_j_s_o_n_encoder_2 = module_0.AnsibleJSONEncoder(int_1, int_1)
        dict_0 = {}
        ansible_j_s_o_n_encoder_3 = module_0.AnsibleJSONEncoder(ansible_j_s_o_n_encoder_2, dict_0)
        ansible_j_s_o_n_encoder_4 = module_0.AnsibleJSONEncoder()
        ansible_j_s_o_n_encoder_5 = module_0.AnsibleJSONEncoder(dict_0, ansible_j_s_o_n_encoder_3)
        list_0 = []
        var_2 = ansible_j_s_o_n_encoder_3.iterencode(list_0)
        str_1 = 'qLMtd'
        int_2 = 656000
        set_0 = {int_2, int_2, ansible_j_s_o_n_encoder_5, str_1}
        var_3 = ansible_j_s_o_n_encoder_3.iterencode(set_0)
        str_2 = 'gnu'
        float_0 = -497.3
        dict_1 = {str_2: str_1, str_1: float_0}
        var_4 = ansible_j_s_o_n_encoder_1.default(dict_1)

if __name__ == "__main__":
    unittest.main()
