import unittest
import timeout_decorator
import ansible.plugins.connection.paramiko_ssh as module_0

class Test_Paramiko_ssh_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = True
            list_0 = [bool_0, bool_0, bool_0]
            int_0 = -2504
            my_add_policy_0 = module_0.MyAddPolicy(list_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
