import unittest
import timeout_decorator
import ansible.plugins.become.su as module_0

class Test_Su_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            tuple_0 = ()
            set_0 = {tuple_0, tuple_0, tuple_0}
            bytes_0 = b'\x05'
            become_module_0 = module_0.BecomeModule()
            var_0 = become_module_0.build_become_command(set_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
