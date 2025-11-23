import unittest
import timeout_decorator
import ansible.parsing.ajson as module_0
import ansible.utils.unsafe_proxy as module_1

class Test_Ajson_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
        bool_0 = False
        dict_0 = {ansible_j_s_o_n_decoder_0: ansible_j_s_o_n_decoder_0, bool_0: bool_0}
        var_0 = ansible_j_s_o_n_decoder_0.object_hook(dict_0)

if __name__ == "__main__":
    unittest.main()
