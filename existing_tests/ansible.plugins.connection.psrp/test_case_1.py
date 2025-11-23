import unittest
import timeout_decorator
import ansible.plugins.connection.psrp as module_0

class Test_Psrp_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'y'
        list_0 = [str_0, str_0, str_0, str_0]
        connection_0 = module_0.Connection(*list_0)
        var_0 = connection_0.reset()

if __name__ == "__main__":
    unittest.main()
