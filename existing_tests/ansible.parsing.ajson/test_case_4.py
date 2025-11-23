import unittest
import timeout_decorator
import ansible.parsing.ajson as module_0
import ansible.utils.unsafe_proxy as module_1

class Test_Ajson_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '__ansible_vault'
        str_1 = 'encrypted_value'
        str_2 = {str_0: str_1}
        str_3 = '__ansible_unsafe'
        str_4 = 'unsafe_value'
        str_5 = {str_3: str_4}
        str_6 = 'key'
        str_7 = 'normal_value'
        str_8 = {str_6: str_7}
        ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
        var_0 = ansible_j_s_o_n_decoder_0.object_hook(str_2)
        var_1 = ansible_j_s_o_n_decoder_0.object_hook(str_5)
        var_2 = module_1.wrap_var(str_4)
        var_3 = ansible_j_s_o_n_decoder_0.object_hook(str_8)

if __name__ == "__main__":
    unittest.main()
