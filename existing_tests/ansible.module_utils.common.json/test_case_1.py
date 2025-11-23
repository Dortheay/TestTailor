import unittest
import timeout_decorator
import ansible.module_utils.common.json as module_0

class Test_Json_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
            int_0 = 167
            ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder()
            var_0 = ansible_j_s_o_n_encoder_1.iterencode(int_0)
            int_1 = 5310
            ansible_j_s_o_n_encoder_2 = module_0.AnsibleJSONEncoder(int_1, int_1)
            dict_0 = {}
            ansible_j_s_o_n_encoder_3 = module_0.AnsibleJSONEncoder(ansible_j_s_o_n_encoder_2, dict_0)
            ansible_j_s_o_n_encoder_4 = module_0.AnsibleJSONEncoder()
            list_0 = []
            var_1 = ansible_j_s_o_n_encoder_3.iterencode(list_0)
            var_2 = ansible_j_s_o_n_encoder_1.default(ansible_j_s_o_n_encoder_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
