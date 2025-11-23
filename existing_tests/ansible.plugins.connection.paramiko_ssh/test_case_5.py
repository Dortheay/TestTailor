import unittest
import timeout_decorator
import ansible.plugins.connection.paramiko_ssh as module_0

class Test_Paramiko_ssh_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = 92
            str_0 = 'xx'
            bytes_0 = b'\x02qZO\xdf\x1b\x00\x073-'
            str_1 = 'r$f_a=Ys(i,lnr\n,UeG'
            list_0 = [bytes_0, bytes_0]
            str_2 = '~4b%|'
            dict_0 = {str_1: bytes_0, str_2: str_2}
            connection_0 = module_0.Connection(bytes_0, str_1, *list_0, **dict_0)
            var_0 = connection_0.put_file(int_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
