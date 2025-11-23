import unittest
import timeout_decorator
import ansible.template.native_helpers as module_0

class Test_Native_helpers_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'ECd@`mn\x0b(QaxdO%0'
        list_0 = [str_0, str_0]
        var_0 = module_0.ansible_native_concat(list_0)

if __name__ == "__main__":
    unittest.main()
