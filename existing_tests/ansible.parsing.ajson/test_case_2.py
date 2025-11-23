import unittest
import timeout_decorator
import ansible.parsing.ajson as module_0
import ansible.utils.unsafe_proxy as module_1

class Test_Ajson_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        dict_0 = {}
        ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
        var_0 = ansible_j_s_o_n_decoder_0.object_hook(dict_0)

if __name__ == "__main__":
    unittest.main()
