import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = 1267.3
            set_0 = {float_0, float_0, float_0}
            str_0 = '`k#\x0b'
            group_0 = module_0.Group(str_0)
            var_0 = group_0.__setstate__(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
