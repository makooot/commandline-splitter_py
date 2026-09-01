import typing
import unittest

from commandline_splitter import splitter


class TestCommandlineSplitter(unittest.TestCase):
    @typing.override
    def setUp(self):
        pass

    def test_empty(self):
        splitted = splitter.splitter("")
        self.assertEqual(splitted, [])

    def test_spaces(self):
        splitted = splitter.splitter("    ")
        self.assertEqual(splitted, [])

    def test_1_token(self):
        splitted = splitter.splitter("abc")
        self.assertEqual(splitted, ["abc"])

    def test_2_tokens(self):
        splitted = splitter.splitter("abc def")
        self.assertEqual(splitted, ["abc", "def"])

    def test_3_tokens(self):
        splitted = splitter.splitter("abc def ghi")
        self.assertEqual(splitted, ["abc", "def", "ghi"])

    def test_spaces_before_tokens(self):
        splitted = splitter.splitter("    abc def ghi")
        self.assertEqual(splitted, ["abc", "def", "ghi"])

    def test_spaces_after_tokens(self):
        splitted = splitter.splitter("abc def ghi    ")
        self.assertEqual(splitted, ["abc", "def", "ghi"])

    def test_backslash_any(self):
        splitted = splitter.splitter(r"a\bc")
        self.assertEqual(splitted, ["abc"])

    def test_backslash_space(self):
        splitted = splitter.splitter(r"abc\ def")
        self.assertEqual(splitted, ["abc def"])

    def test_single_quote(self):
        splitted = splitter.splitter(r"'abc'")
        self.assertEqual(splitted, ["abc"])

    def test_single_quote_wrap_space(self):
        splitted = splitter.splitter(r"'abc def'")
        self.assertEqual(splitted, ["abc def"])

    def test_single_quote_wrap_backslash(self):
        splitted = splitter.splitter(r"'g\hi'")
        self.assertEqual(splitted, [r"g\hi"])

    def test_single_quote_wrap_couble_quote(self):
        splitted = splitter.splitter(r"""'jk"l'""")
        self.assertEqual(splitted, ['jk"l'])

    def test_double_quote(self):
        splitted = splitter.splitter(r'"abc"')
        self.assertEqual(splitted, ["abc"])

    def test_double_quote_wrap_space(self):
        splitted = splitter.splitter(r'"abc def"')
        self.assertEqual(splitted, ["abc def"])

    def test_double_quote_wrap_backslash(self):
        splitted = splitter.splitter(r'"g\hi"')
        self.assertEqual(splitted, ["ghi"])

    def test_double_quote_wrap_single_quote(self):
        splitted = splitter.splitter(r'''"It's"''')
        self.assertEqual(splitted, ["It's"])

    def test_unclosed_single_quote(self):
        splitted = splitter.splitter(r"'abc")
        self.assertEqual(splitted, ["abc"])

    def test_unclosed_double_quote(self):
        splitted = splitter.splitter(r'"abc')
        self.assertEqual(splitted, ["abc"])

    def test_backslash_no_following(self):
        splitted = splitter.splitter("abc\\")
        self.assertEqual(splitted, ["abc"])

    def test_unclosed_double_quote_backslash_no_following(self):
        splitted = splitter.splitter('"abc\\')
        self.assertEqual(splitted, ["abc"])

    def test_mix_1(self):
        splitted = splitter.splitter(r""" say --pre=T\ T "foo's bar" '\10,000' """)
        self.assertEqual(splitted, ["say", "--pre=T T", "foo's bar", r"\10,000"])
