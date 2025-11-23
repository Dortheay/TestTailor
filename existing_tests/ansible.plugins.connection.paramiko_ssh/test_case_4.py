import unittest
import timeout_decorator
import ansible.plugins.connection.paramiko_ssh as module_0

class Test_Paramiko_ssh_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            list_0 = None
            dict_0 = {list_0: list_0}
            bytes_0 = b'{\xc5[wU\xaa\xc3o\x08\xea\x84Ew* \\?<1'
            list_1 = [bytes_0, dict_0, bytes_0]
            connection_0 = module_0.Connection(dict_0, bytes_0, *list_1)
            var_0 = connection_0.reset()
            str_0 = 'u`'
            set_0 = {bytes_0, str_0}
            connection_1 = module_0.Connection(connection_0, set_0, *list_1)
            var_1 = connection_1.exec_command(list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
