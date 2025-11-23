import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = "2w\n(\x0b'qItbZWlZ"
            group_0 = module_0.Group()
            var_0 = group_0.set_priority(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
