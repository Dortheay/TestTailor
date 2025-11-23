import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        int_0 = 80
        str_0 = '\x0by]7So'
        str_1 = 'j]rH#c3xb/)1'
        var_0 = module_0.append_tcp_flags(str_0, str_1, int_0)

if __name__ == "__main__":
    unittest.main()
