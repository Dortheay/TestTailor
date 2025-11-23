import unittest
import timeout_decorator
import pytutils.lazy.lazy_import as module_0

class Test_Lazy_import_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = '{cls_name}({name})'
            float_0 = -575.641067
            float_1 = 1345.0
            illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(float_0, float_1)
            var_0 = illegal_use_of_scope_replacer_0.__eq__(illegal_use_of_scope_replacer_0)
            var_1 = illegal_use_of_scope_replacer_0.__eq__(str_0)
            bytes_0 = b'\xb2\xe5v\xafC\xc0 \x9b\xa1\xd4kl'
            import_processor_0 = module_0.ImportProcessor()
            var_2 = import_processor_0.lazy_import(illegal_use_of_scope_replacer_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
