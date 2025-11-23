import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '\tzVwvgIpv=9U\r%tv'
        group_0 = module_0.Group(str_0)

if __name__ == "__main__":
    unittest.main()
