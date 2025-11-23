import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            bytes_0 = b'\x16#\xc1\xc2\xf30'
            set_0 = {bytes_0, bytes_0}
            list_0 = [bytes_0, set_0, set_0, set_0]
            bool_0 = False
            var_0 = module_1.rekey_on_member(list_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
