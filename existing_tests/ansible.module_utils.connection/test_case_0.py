import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = "#?hmWk&>:JQdi*'AY]\x0b$"
            set_0 = {str_0, str_0, str_0, str_0}
            var_0 = module_0.write_to_file_descriptor(set_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
