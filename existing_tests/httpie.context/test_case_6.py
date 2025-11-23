import unittest
import timeout_decorator
import httpie.context as module_0

class Test_Context_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'V'
            str_1 = 'KeyValueArg'
            environment_0 = module_0.Environment()
            var_0 = environment_0.__str__()
            environment_1 = module_0.Environment(str_1)
            str_2 = ')zPKyfL0'
            var_1 = environment_1.__repr__()
            str_3 = '\n    Prints the exception traceback should one occur, as well as other\n    information useful for debugging HTTPie itself and for reporting bugs.\n\n    '
            var_2 = environment_1.__repr__()
            var_3 = environment_1.__repr__()
            str_4 = 'Y9B\x0cO:at'
            dict_0 = {str_0: str_0, str_2: str_0, str_3: str_0, str_4: str_0}
            var_4 = environment_1.log_error(environment_1)
            environment_2 = module_0.Environment(dict_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
