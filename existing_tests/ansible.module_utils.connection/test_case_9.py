import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = "]'V?/n.KaFZThstNZB"
            bool_0 = True
            list_0 = [str_0, str_0]
            list_1 = [bool_0, list_0, bool_0]
            tuple_0 = ()
            connection_0 = module_0.Connection(tuple_0)
            var_0 = connection_0.__getattr__(list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
