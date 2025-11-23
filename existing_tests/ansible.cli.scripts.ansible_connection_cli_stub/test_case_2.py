import unittest
import timeout_decorator
import ansible.cli.scripts.ansible_connection_cli_stub as module_0

class Test_Ansible_connection_cli_stub_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = True
            bytes_0 = b'\xda\x82\x93\x9bv\x9a=i'
            int_0 = 24
            set_0 = {int_0}
            list_0 = []
            str_0 = 'Using run_once with the free strategy is not currently supported. This task will still be executed for every host in the inventory list.'
            connection_process_0 = module_0.ConnectionProcess(bytes_0, int_0, set_0, list_0, str_0)
            var_0 = connection_process_0.start(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
