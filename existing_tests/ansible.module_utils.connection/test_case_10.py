import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'Unable to read sysctl: %s'
            connection_0 = module_0.Connection(str_0)
            dict_0 = {connection_0: connection_0, connection_0: connection_0}
            var_0 = module_0.write_to_file_descriptor(connection_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
