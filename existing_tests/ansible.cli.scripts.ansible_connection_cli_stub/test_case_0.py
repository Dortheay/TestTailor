import unittest
import timeout_decorator
import ansible.cli.scripts.ansible_connection_cli_stub as module_0

class Test_Ansible_connection_cli_stub_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        complex_0 = None
        bool_0 = True
        list_0 = [complex_0, complex_0, bool_0, bool_0]
        connection_process_0 = module_0.ConnectionProcess(list_0, bool_0, list_0, list_0)

if __name__ == "__main__":
    unittest.main()
