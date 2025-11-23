import unittest
import timeout_decorator
import ansible.module_utils.compat.selinux as module_0

class Test_Selinux_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'=M\x93\x1c\xe8\xe0\xcf\xac\x91\xf9\x04'
            var_0 = module_0.lgetfilecon_raw(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
