import unittest
import timeout_decorator
import ansible.modules.cron as module_0

class Test_Cron_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = False
            cron_tab_0 = module_0.CronTab(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
