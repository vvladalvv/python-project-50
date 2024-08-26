# gendiff/scripts/gendiff.py
import argparse

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')

    parser.add_argument('-f', '--format', help='set format of output', default='stylish')

    args = parser.parse_args()

    print(f"Comparing {args.first_file} and {args.second_file}")
    print(f"Output format: {args.format}")


if __name__ == '__main__':
    main()