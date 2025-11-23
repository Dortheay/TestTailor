import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            dict_0 = {}
            str_0 = '{cls_nme}({name})'
            tuple_0 = ()
            float_0 = -493.0
            list_0 = []
            import_replacer_0 = module_0.ImportReplacer(dict_0, float_0, list_0)
            scope_replacer_0 = module_0.ScopeReplacer(dict_0, import_replacer_0, str_0)
            var_0 = scope_replacer_0.__getattribute__(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
