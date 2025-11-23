import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            list_0 = None
            set_0 = {list_0, list_0, list_0, list_0}
            str_0 = '\r.od\nWw0U{\r&_|(<El[B'
            connection_0 = module_0.Connection(str_0)
            var_0 = connection_0.send(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
