import unittest
import timeout_decorator
import thefuck.corrector as module_0

class Test_Corrector_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            var_0 = module_0.get_rules_import_paths()
            var_1 = module_0.get_rules_import_paths()
            bytes_0 = b'\x85@\x1d^\x9bdW\xdb\xd4Xm\xca\xf8a\x18\x87\xe1\xbb\xaf'
            dict_0 = None
            var_2 = module_0.organize_commands(dict_0)
            var_3 = module_0.get_corrected_commands(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
