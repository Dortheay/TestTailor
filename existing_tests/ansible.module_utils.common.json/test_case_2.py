import unittest
import timeout_decorator
import ansible.module_utils.common.json as module_0

class Test_Json_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
            bytes_0 = b'\xfc\x16\xad\x9d\x880\x8c\x99K\x8f\n<\xb8\xd9Fw\xab\x91\x8c\xb6'
            var_0 = ansible_j_s_o_n_encoder_0.default(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
