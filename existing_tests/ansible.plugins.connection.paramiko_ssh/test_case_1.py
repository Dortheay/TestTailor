import unittest
import timeout_decorator
import ansible.plugins.connection.paramiko_ssh as module_0

class Test_Paramiko_ssh_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            connection_0 = module_0.Connection()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
