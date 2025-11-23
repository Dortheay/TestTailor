import unittest
import timeout_decorator
import ansible.executor.play_iterator as module_0

class Test_Play_iterator_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\x04J\x0ceC\xe7n9\xb1'
            bytes_1 = b'\x17J\x13\x98\x80R-\xea\x7f\\AN \x8f!'
            str_0 = '<\x0bz*8\t*\r#VcV'
            list_0 = []
            bool_0 = True
            bool_1 = False
            play_iterator_0 = module_0.PlayIterator(bytes_0, bytes_1, str_0, list_0, bool_0, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
