import unittest
import timeout_decorator
import ansible.playbook.play as module_0

class Test_Play_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\xa6\x02\xc1\x1fX'
            play_0 = module_0.Play()
            var_0 = play_0.load(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
