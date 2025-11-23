import unittest
import timeout_decorator
import ansible.playbook.included_file as module_0

class Test_Included_file_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        list_0 = []
        bytes_0 = b'\x97F\x00\xd2w\x1a\x1f\xa9I\x13Dlo\xd8\xb4,(\xb1'
        str_0 = 'Q;LXa$PM(\rPE`N'
        included_file_0 = module_0.IncludedFile(list_0, list_0, bytes_0, str_0)

if __name__ == "__main__":
    unittest.main()
