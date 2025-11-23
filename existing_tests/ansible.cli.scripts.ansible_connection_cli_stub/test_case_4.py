import unittest
import timeout_decorator
import ansible.cli.scripts.ansible_connection_cli_stub as module_0

class Test_Ansible_connection_cli_stub_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = 813.3
            dict_0 = None
            tuple_0 = ()
            tuple_1 = (tuple_0,)
            tuple_2 = ()
            dict_1 = {tuple_1: tuple_1, tuple_2: tuple_2, tuple_2: tuple_2}
            str_0 = 'ansible.cli.scripts.ansible_connection_cli_stub'
            list_0 = [str_0, tuple_0, tuple_0]
            connection_process_0 = module_0.ConnectionProcess(tuple_1, dict_1, str_0, list_0)
            var_0 = connection_process_0.connect_timeout(float_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
