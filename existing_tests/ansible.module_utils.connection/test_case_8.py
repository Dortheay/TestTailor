import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '\x0c\x0b;%>C)'
            str_1 = 'num_pvs'
            list_0 = [str_1]
            connection_0 = module_0.Connection(list_0)
            var_0 = connection_0.send(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
