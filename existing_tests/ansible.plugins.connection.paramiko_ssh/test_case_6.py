import unittest
import timeout_decorator
import ansible.plugins.connection.paramiko_ssh as module_0

class Test_Paramiko_ssh_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = 462
            bytes_0 = b'\xb0\x95\xc8\x16\xef\xfdUn\xa0\x83)\xb3"n\x10\x15\x8f'
            tuple_0 = (int_0, bytes_0)
            int_1 = 640
            str_0 = '('
            dict_0 = {str_0: int_1, str_0: tuple_0}
            connection_0 = module_0.Connection(tuple_0, int_1, dict_0)
            var_0 = connection_0.reset()
            bool_0 = True
            str_1 = 'wUN.j+{!F\rkkX'
            var_1 = connection_0.fetch_file(bool_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
