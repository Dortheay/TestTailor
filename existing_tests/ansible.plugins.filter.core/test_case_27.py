import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        try:
            list_0 = None
            str_0 = None
            str_1 = 'Oos\r)%'
            var_0 = module_0.rand(list_0, str_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
