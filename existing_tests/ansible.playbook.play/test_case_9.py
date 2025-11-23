import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        play_0 = module_0.Play()
        str_0 = 'included_path'
        str_1 = 'action_groups'
        str_2 = 'group_actions'
        str_3 = 'roles'
        str_4 = '/path/to/included/file'
        str_5 = 'group1'
        str_6 = 'action1'
        str_7 = 'action2'
        str_8 = [str_6, str_7]
        str_9 = {str_5: str_8}
        str_10 = {str_6: str_5}
        str_11 = 'name'
        str_12 = 'path'
        str_13 = 'role1'
        str_14 = '/path/to/role1'
        str_15 = {str_11: str_13, str_12: str_14}
        str_16 = 'role2'
        str_17 = '/path/to/role2'
        str_18 = {str_11: str_16, str_12: str_17}
        str_19 = [str_15, str_18]
        str_20 = {str_0: str_4, str_1: str_9, str_2: str_10, str_3: str_19}
        var_0 = play_0.deserialize(str_20)
        var_1 = play_0.roles
        var_2 = len(var_1)

if __name__ == "__main__":
    unittest.main()
