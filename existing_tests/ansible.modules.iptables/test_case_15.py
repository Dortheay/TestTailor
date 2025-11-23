import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'vRx'
            str_1 = '5\\{w>lWX\rz7=]UMi@'
            list_0 = [str_1, str_1, str_1, str_1]
            bool_0 = True
            var_0 = module_0.append_match(str_0, list_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
