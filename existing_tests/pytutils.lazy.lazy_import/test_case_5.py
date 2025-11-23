import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            scope_replacer_0 = None
            str_0 = None
            str_1 = "Return a member from the proxied regex object.\n\n        If the regex hasn't been compiled yet, compile it\n        "
            str_2 = None
            dict_0 = {str_0: scope_replacer_0, str_1: str_1, str_2: str_0, str_2: scope_replacer_0}
            list_0 = [dict_0, dict_0, scope_replacer_0, dict_0]
            bool_0 = True
            float_0 = -1019.81
            bytes_0 = b'\x9c\xa6\xfcUM\x1dU/'
            import_replacer_0 = module_0.ImportReplacer(list_0, bool_0, float_0, bytes_0)
            illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(dict_0, import_replacer_0, import_replacer_0)
            var_0 = illegal_use_of_scope_replacer_0.__unicode__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
