import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\x80N\x101\xa6\xc3\x9d'
            group_0 = module_0.Group()
            var_0 = group_0.add_child_group(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
