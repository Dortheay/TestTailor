import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            list_0 = []
            list_1 = [list_0, list_0, list_0, list_0]
            var_0 = module_0.flatten(list_1)
            bytes_0 = b'\xd2\x93\x9b\xf1\x12\xb0\xc0_\xa7\x819(W\x0f\xfaE\x0c'
            list_2 = None
            list_3 = [bytes_0, list_2, list_2, bytes_0]
            var_1 = module_0.from_yaml_all(list_3)
            var_2 = module_0.get_encrypted_password(bytes_0, list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
