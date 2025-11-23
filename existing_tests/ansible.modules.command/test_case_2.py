import unittest
import timeout_decorator
import ansible.modules.command as module_0

class Test_Command_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 19
            set_0 = {int_0}
            bytes_0 = b'\x92H\x8f\xed\xe6O\xe2\xc2\xdfg\x07`\xd9'
            var_0 = module_0.check_command(set_0, bytes_0)
            str_0 = '@[0*sM\nv~m'
            bool_0 = True
            tuple_0 = (str_0, bool_0)
            list_0 = [tuple_0]
            var_1 = module_0.check_command(tuple_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
