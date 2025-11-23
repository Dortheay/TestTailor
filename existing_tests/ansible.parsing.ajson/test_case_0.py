import unittest
import timeout_decorator
import ansible.parsing.ajson as module_0

class Test_Ajson_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '__ansible_vault'
            str_1 = {str_0: str_0}
            str_2 = 'normal_value'
            ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
            var_0 = ansible_j_s_o_n_decoder_0.object_hook(str_1)
            var_1 = ansible_j_s_o_n_decoder_0.object_hook(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
