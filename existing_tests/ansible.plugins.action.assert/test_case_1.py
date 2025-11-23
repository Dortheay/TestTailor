import unittest
import timeout_decorator
import ansible.plugins.action.assert as module_0

class Test_Assert_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 2539
            list_0 = []
            int_1 = 65536
            str_0 = '!,Z\tW1Xw@L,v3:X'
            bytes_0 = b'w\xd8\\n\xd0\xb4]\x8f\xde\x04'
            action_module_0 = module_0.ActionModule(int_0, list_0, int_1, str_0, list_0, bytes_0)
            var_0 = action_module_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
