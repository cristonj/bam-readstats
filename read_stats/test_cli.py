import sys
import unittest

from cli import parse_args

class TestCLI(unittest.TestCase):
    def test_parse_args_success(self):
        # All required arguments provided, plus optional --bed
        test_args = ['prog', '--bam', 'input.bam', '--output', 'outdir', '--bed', 'regions.bed']
        sys.argv = test_args
        args = parse_args()
        self.assertEqual(args.bam, 'input.bam')
        self.assertEqual(args.output, 'outdir')
        self.assertEqual(args.bed, 'regions.bed')

    def test_parse_args_success_without_optional_bed(self):
        # Required arguments only, without --bed
        test_args = ['prog', '--bam', 'input.bam', '--output', 'outdir']
        sys.argv = test_args
        args = parse_args()
        self.assertEqual(args.bam, 'input.bam')
        self.assertEqual(args.output, 'outdir')
        self.assertIsNone(args.bed)

    def test_parse_args_missing_bam(self):
        # Missing required argument --bam
        test_args = ['prog', '--output', 'outdir']
        sys.argv = test_args
        with self.assertRaises(SystemExit):
            parse_args()

    def test_parse_args_missing_output(self):
        # Missing required argument --output
        test_args = ['prog', '--bam', 'input.bam']
        sys.argv = test_args
        with self.assertRaises(SystemExit):
            parse_args()

if __name__ == '__main__':
    unittest.main()

