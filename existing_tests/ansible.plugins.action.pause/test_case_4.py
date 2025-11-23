import unittest
import timeout_decorator
import ansible.plugins.action.pause as module_0

class Test_Pause_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = None
            list_0 = [bytes_0, bytes_0, bytes_0]
            var_0 = module_0.clear_line(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
