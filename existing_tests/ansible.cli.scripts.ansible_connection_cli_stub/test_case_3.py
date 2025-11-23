import unittest
import timeout_decorator
import ansible.cli.scripts.ansible_connection_cli_stub as module_0

class Test_Ansible_connection_cli_stub_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'bIYp'
            tuple_0 = ()
            int_0 = 1
            set_0 = {str_0, str_0, tuple_0, int_0}
            connection_process_0 = module_0.ConnectionProcess(str_0, tuple_0, str_0, str_0, set_0)
            var_0 = connection_process_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
