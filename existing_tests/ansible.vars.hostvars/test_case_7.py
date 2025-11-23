import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bytes_0 = b'\xff+\x8d\xfaBx\xbd\xdf.\x87\x0b\x18\xf1\xf1S'
            bytes_1 = b"\x8c\x8aS3'|\xf5\xae\x8f\x08"
            dict_0 = {}
            host_vars_vars_0 = module_0.HostVarsVars(bytes_1, dict_0)
            var_0 = host_vars_vars_0.__getitem__(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
