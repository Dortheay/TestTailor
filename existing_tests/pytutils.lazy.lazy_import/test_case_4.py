import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '60duQv{Dc_;vlwsm)]$ '
            str_1 = '\rO"'
            str_2 = 'uDb@hj#y\njtk)3'
            dict_0 = {str_0: str_0, str_1: str_0, str_2: str_0, str_2: str_1}
            list_0 = None
            illegal_use_of_scope_replacer_0 = None
            illegal_use_of_scope_replacer_1 = module_0.IllegalUseOfScopeReplacer(list_0, str_2)
            dict_1 = {str_0: dict_0, illegal_use_of_scope_replacer_0: illegal_use_of_scope_replacer_1}
            import_processor_0 = module_0.ImportProcessor(illegal_use_of_scope_replacer_0)
            float_0 = -1317.0
            bytes_0 = b'0\xea7\xc9'
            tuple_0 = (float_0, bytes_0)
            import_replacer_0 = module_0.ImportReplacer(list_0, illegal_use_of_scope_replacer_0, dict_1, import_processor_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
