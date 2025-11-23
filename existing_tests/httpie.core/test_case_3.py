import unittest
import timeout_decorator
import httpie.core as module_0
import httpie.context as module_1

class Test_Core_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'h\nx\nOC.sIRaF'
        str_1 = ''
        exit_status_0 = module_0.main()
        dict_0 = {str_0: str_0, str_1: str_0}
        exit_status_1 = module_0.main(dict_0)

if __name__ == "__main__":
    unittest.main()
