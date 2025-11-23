import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            import_processor_0 = module_0.ImportProcessor()
            list_0 = []
            dict_0 = {}
            str_0 = 'z'
            list_1 = [str_0]
            str_1 = '3iD,b|!.\x0cxX~'
            scope_replacer_0 = module_0.ScopeReplacer(dict_0, list_1, str_1)
            import_processor_1 = module_0.ImportProcessor()
            var_0 = import_processor_1.lazy_import(list_0, scope_replacer_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
