import unittest
import timeout_decorator
import ansible.cli.scripts.ansible_connection_cli_stub as module_0

class Test_Ansible_connection_cli_stub_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bool_0 = False
            str_0 = ''
            set_0 = {str_0}
            float_0 = 90.0
            connection_process_0 = module_0.ConnectionProcess(bool_0, set_0, float_0, str_0)
            bytes_0 = b'\x92\xdb\xe7\xb0\x19\xdc\xd0\x01\x03'
            str_1 = '8ffbAG_D2u'
            var_0 = connection_process_0.handler(bytes_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
