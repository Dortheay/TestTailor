import unittest
import timeout_decorator
import ansible.modules.lineinfile as module_0

class Test_Lineinfile_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'vBs*VZV\\7M:)U$/G4N;o'
            bytes_0 = b' \xeb'
            set_0 = {bytes_0, bytes_0, str_0}
            var_0 = module_0.write_changes(str_0, bytes_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
