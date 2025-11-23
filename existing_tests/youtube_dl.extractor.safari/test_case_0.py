import unittest
import timeout_decorator
import youtube_dl.extractor.safari as module_0

class Test_Safari_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        safari_course_i_e_0 = module_0.SafariCourseIE()

if __name__ == "__main__":
    unittest.main()
