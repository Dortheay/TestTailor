import unittest
import timeout_decorator
import ansible.cli.scripts.ansible_connection_cli_stub as module_0

class Test_Ansible_connection_cli_stub_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '__main__'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
            set_0 = set()
            complex_0 = None
            tuple_0 = (complex_0, complex_0)
            bytes_0 = b'\x87\x18N\xc5F\xdbAU(\x9f\x1eSs\xe4Uur\xbc'
            connection_process_0 = module_0.ConnectionProcess(tuple_0, complex_0, bytes_0, tuple_0)
            var_0 = connection_process_0.command_timeout(dict_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
