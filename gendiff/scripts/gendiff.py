# gendiff/scripts/gendiff.py
import argparse
from gendiff import generate_diff
# import os


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')
    parser.add_argument('-f', '--format', help='set format of output', default='stylish')

    args = parser.parse_args()

    # current_dir = os.getcwd()
    # first_file_path = os.path.abspath(os.path.join(current_dir, args.first_file))
    # second_file_path = os.path.abspath(os.path.join(current_dir, args.second_file))

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

    # print(f"Comparing {args.first_file} and {args.second_file}")
    # print(f"Output format: {args.format}")


if __name__ == '__main__':
    main()