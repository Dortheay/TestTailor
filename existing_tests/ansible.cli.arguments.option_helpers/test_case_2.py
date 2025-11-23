import unittest
import timeout_decorator
import ansible.cli.arguments.option_helpers as module_0

class Test_Option_helpers_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'WORKER HARD EXIT: %s'
            list_0 = []
            str_1 = ')'
            ansible_version_0 = None
            unrecognized_argument_0 = module_0.UnrecognizedArgument(list_0, str_1, ansible_version_0)
            bool_0 = False
            int_0 = -8
            bytes_0 = b'\xed\xc7<\r`\xe9\xdcG\xf4@\x85\xf9\x19\x83\xb2\xdb\xa3'
            set_0 = {int_0, int_0, bytes_0}
            bool_1 = False
            str_2 = 'frV|{l 3^u;ORyu@ ]|)'
            float_0 = 0.2
            int_1 = 3775
            list_1 = [int_1]
            tuple_0 = (set_0, bytes_0, float_0, list_1)
            bool_2 = False
            str_3 = 'Yj_}0~ZKv 2n5:&m'
            ansible_version_1 = module_0.AnsibleVersion(str_3, str_3)
            bool_3 = False
            unrecognized_argument_1 = module_0.UnrecognizedArgument(set_0, bool_2, ansible_version_1, bool_3)
            list_2 = [bool_1, bool_2, float_0, bool_2]
            unrecognized_argument_2 = module_0.UnrecognizedArgument(str_2, tuple_0, unrecognized_argument_1, list_2, unrecognized_argument_1)
            bool_4 = False
            ansible_version_2 = module_0.AnsibleVersion(unrecognized_argument_2, str_3, bool_2, bool_4)
            ansible_version_3 = module_0.AnsibleVersion(int_0, set_0, bool_1, bool_1, ansible_version_2)
            var_0 = ansible_version_3.__call__(str_0, unrecognized_argument_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
