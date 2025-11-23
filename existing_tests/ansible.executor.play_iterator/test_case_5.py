import unittest
import timeout_decorator
import ansible.executor.play_iterator as module_0

class Test_Play_iterator_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            play_iterator_0 = module_0.PlayIterator()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
