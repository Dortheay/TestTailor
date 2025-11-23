import unittest
import timeout_decorator
import ansible.playbook.play_context as module_0

class Test_Play_context_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bytes_0 = b'\x90\xee\xe9\xda\xb4W\t'
            bytes_1 = b'\xd6y9\x83\x93\xa7;l\xb2\x82\xae\xe6\xf2'
            play_context_0 = module_0.PlayContext(bytes_0, bytes_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
