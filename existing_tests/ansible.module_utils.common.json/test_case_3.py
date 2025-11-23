import unittest
import timeout_decorator
import ansible.module_utils.common.json as module_0

class Test_Json_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            list_0 = None
            str_0 = '@Fw;\r\tK;,\r.oq;4V-$'
            str_1 = '\n'
            dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
            ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(dict_0)
            var_0 = ansible_j_s_o_n_encoder_0.iterencode(list_0)
            float_0 = 382.78
            ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder(float_0)
            str_2 = '//\n-'
            list_1 = [ansible_j_s_o_n_encoder_1, ansible_j_s_o_n_encoder_0, str_2]
            var_1 = ansible_j_s_o_n_encoder_1.iterencode(list_1)
            str_3 = 'gszwjn'
            var_2 = ansible_j_s_o_n_encoder_1.default(str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
