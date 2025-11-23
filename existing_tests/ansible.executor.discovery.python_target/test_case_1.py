import unittest
import timeout_decorator
import ansible.executor.discovery.python_target as module_0

class Test_Python_target_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '5\ryhi[5PLz'
        set_0 = set()
        var_0 = module_0.read_utf8_file(str_0, set_0)

if __name__ == "__main__":
    unittest.main()
