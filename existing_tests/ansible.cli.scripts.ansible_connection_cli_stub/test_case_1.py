import unittest
import timeout_decorator
import ansible.cli.scripts.ansible_connection_cli_stub as module_0

class Test_Ansible_connection_cli_stub_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            var_0 = module_0.main()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
