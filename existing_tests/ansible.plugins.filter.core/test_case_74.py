import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_75(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_25(self):
        str_0 = 'Ansible is great, ansible is powerful.'
        str_1 = 'ansible'
        str_2 = 'Python'
        bool_0 = True
        bool_1 = False
        var_0 = module_0.regex_replace(str_0, str_1, str_2, bool_0, bool_1)

if __name__ == "__main__":
    unittest.main()
