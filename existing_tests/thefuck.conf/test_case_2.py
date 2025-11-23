import unittest
import timeout_decorator
import thefuck.conf as module_0

class Test_Conf_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '^mux'
        bool_0 = True
        dict_0 = {str_0: bool_0}
        settings_0 = module_0.Settings(**dict_0)
        str_1 = 'Caches function result in temporary file.\n\n    Cache will be expired when modification date of files from `depends_on`\n    will be changed.\n\n    Only functions should be wrapped in `cache`, not methods.\n\n    '
        var_0 = settings_0.__getattr__(str_1)
        var_1 = settings_0.init(settings_0)

if __name__ == "__main__":
    unittest.main()
