import unittest
import timeout_decorator
import ansible.context as module_0

class Test_Context_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bytes_0 = b''
        var_0 = module_0.cliargs_deferred_get(bytes_0)

if __name__ == "__main__":
    unittest.main()
