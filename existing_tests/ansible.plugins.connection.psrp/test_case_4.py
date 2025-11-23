import unittest
import timeout_decorator
import ansible.plugins.connection.psrp as module_0

class Test_Psrp_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '~llow-unauthenticaged'
            list_0 = [str_0, str_0, str_0, str_0, str_0]
            connection_0 = module_0.Connection(*list_0)
            var_0 = connection_0.close()
            connection_1 = module_0.Connection(*list_0)
            set_0 = {str_0}
            var_1 = connection_1.exec_command(list_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
