"""Interface model unit test

"""

import unittest
from os import walk
from os.path import join
from pathlib import Path

from pylint.lint import Run


class CodeFormatAndQuality(unittest.TestCase):

    MINIMUM_SCORE = 9

    def setUp(self):
        """Searching for all python files to be checked

        """
        self.list_of_files = []
        root = Path(__file__).absolute().parents[1]
        for (directory, _, filenames) in walk(root.as_posix()):
            self.list_of_files += [join(directory, file) for file in filenames
                                   if file.endswith('.py') and not file.startswith('test')]
        self.list_of_files.append('--max-line-length=240')
        self.list_of_files.append(root.parents[0].joinpath('RpcParser/markdown_generator.py').as_posix())

    def test_check(self):
        """Performing checks by PyLint

        """
        results = Run(self.list_of_files, do_exit=False)
        score = results.linter.stats['global_note']
        self.assertGreaterEqual(score, self.MINIMUM_SCORE)


if __name__ == "__main__":
    unittest.main()
