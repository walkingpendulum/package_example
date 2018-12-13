from unittest import TestCase

from palindrome_checker.entrypoints import checker


class CliTestCase(TestCase):
    def test_entry_point_call(self):
        with self.assertRaises(BaseException) as context:
            checker(["-i", "aa"])

        self.assertIsInstance(context.exception, SystemExit)
        self.assertEqual(context.exception.code, 0)

        with self.assertRaises(BaseException) as context:
            checker(["-i", "aac"])

        self.assertIsInstance(context.exception, SystemExit)
        self.assertEqual(context.exception.code, 1)
