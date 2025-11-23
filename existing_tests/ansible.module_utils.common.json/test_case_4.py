import unittest
import timeout_decorator
import ansible.module_utils.common.json as module_0

class Test_Json_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()

if __name__ == "__main__":
    unittest.main()
