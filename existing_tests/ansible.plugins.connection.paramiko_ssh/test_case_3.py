import unittest
import timeout_decorator
import ansible.plugins.connection.paramiko_ssh as module_0

class Test_Paramiko_ssh_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'bk%'
            list_0 = [str_0, str_0, str_0]
            list_1 = [list_0]
            connection_0 = module_0.Connection(str_0, list_0, list_1)
            var_0 = connection_0.close()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
