import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            bytes_0 = b'\x80\xbe\x88\n\xa9\xe7\xac\xbe\xfc\x83\x8c{v\xe6\xb7\xea\xa7\xa0JN'
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_playbook_on_handler_task_start(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
