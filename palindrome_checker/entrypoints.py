import argparse
import sys

import argcomplete

from palindrome_checker import __version__
from palindrome_checker.core import is_palindrome


def checker(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='input', type=str, help='Input string to check.')
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)

    argcomplete.autocomplete(parser)

    args = parser.parse_args(argv)
    palindromity = not is_palindrome(sequence=args.input)
    sys.exit(palindromity)
