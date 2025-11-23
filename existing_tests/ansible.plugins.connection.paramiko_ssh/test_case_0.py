import unittest
import timeout_decorator
import ansible.plugins.connection.paramiko_ssh as module_0

class Test_Paramiko_ssh_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = '/local/path/to/file'
        float_0 = -499.0
        list_0 = [str_0, float_0, str_0]
        connection_0 = module_0.Connection(list_0, str_0, str_0)
        var_0 = connection_0.reset()

if __name__ == "__main__":
    unittest.main()
