import unittest
import timeout_decorator
import ansible.plugins.connection.paramiko_ssh as module_0

class Test_Paramiko_ssh_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            float_0 = -607.336
            list_0 = [float_0, float_0]
            str_0 = '@i!i-_D0v]'
            connection_0 = module_0.Connection(float_0, list_0, str_0)
            list_1 = []
            int_0 = 257
            list_2 = [str_0, connection_0, connection_0]
            list_3 = [list_2, float_0]
            my_add_policy_0 = module_0.MyAddPolicy(list_3, connection_0)
            var_0 = my_add_policy_0.missing_host_key(connection_0, list_1, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
