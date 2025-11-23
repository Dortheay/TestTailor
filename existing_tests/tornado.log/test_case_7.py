import unittest
import timeout_decorator
import tornado.log as module_0
import logging as module_1

class Test_Log_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            float_0 = 232.1
            str_0 = 'Runs multiple asynchronous operations in parallel.\n\n    ``children`` may either be a list or a dict whose values are\n    yieldable objects. ``multi()`` returns a new yieldable\n    object that resolves to a parallel structure containing their\n    results. If ``children`` is a list, the result is a list of\n    results in the same order; if it is a dict, the result is a dict\n    with the same keys.\n\n    That is, ``results = yield multi(list_of_futures)`` is equivalent\n    to::\n\n        results = []\n        for future in list_of_futures:\n            results.append(yield future)\n\n    If any children raise exceptions, ``multi()`` will raise the first\n    one. All others will be logged, unless they are of types\n    contained in the ``quiet_exceptions`` argument.\n\n    In a ``yield``-based coroutine, it is not normally necessary to\n    call this function directly, since the coroutine runner will\n    do it automatically when a list or dict is yielded. However,\n    it is necessary in ``await``-based coroutines, or to pass\n    the ``quiet_exceptions`` argument.\n\n    This function is available under the names ``multi()`` and ``Multi()``\n    for historical reasons.\n\n    Cancelling a `.Future` returned by ``multi()`` does not cancel its\n    children. `asyncio.gather` is similar to ``multi()``, but it does\n    cancel its children.\n\n    .. versionchanged:: 4.2\n       If multiple yieldables fail, any exceptions after the first\n       (which is raised) will be logged. Added the ``quiet_exceptions``\n       argument to suppress this logging for selected exception types.\n\n    .. versionchanged:: 4.3\n       Replaced the class ``Multi`` and the function ``multi_future``\n       with a unified function ``multi``. Added support for yieldables\n       other than ``YieldPoint`` and `.Future`.\n\n    '
            bool_0 = False
            dict_0 = {}
            log_formatter_0 = module_0.LogFormatter(str_0, str_0, bool_0, dict_0)
            str_1 = log_formatter_0.format(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
