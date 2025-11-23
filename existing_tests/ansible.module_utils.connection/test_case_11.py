import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            int_0 = -1197
            bytes_0 = b'\xb4\xc0%\xa2}\xa7\xd5'
            bool_0 = False
            list_0 = [int_0, bytes_0, bool_0, bool_0]
            var_0 = module_0.write_to_file_descriptor(bool_0, list_0)
            connection_0 = module_0.Connection(bytes_0)
            var_1 = module_0.recv_data(connection_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
