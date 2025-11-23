import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'TyMf|Do4]r9\n'
            tuple_0 = module_0.parse_host(str_0)
            list_0 = [tuple_0, str_0, str_0, str_0]
            dict_0 = module_0.fwd_normalize(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
