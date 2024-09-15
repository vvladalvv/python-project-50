# gendiff/scripts/gendiff.py
import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='''
    Compares two configuration files and shows a difference.''')
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    return diff


if __name__ == '__main__':
    main()
