"""
Implementation of grep command using python script
"""

import os
import argparse
import re
import glob


def grep(char, files, dir_name):
    try:
        char_to_search = re.compile(r'.*{}.*'.format(char))
        os.chdir(dir_name)
        search_files = glob.glob(files)
        for file in search_files:
            with open(file, 'r', encoding='utf-8') as f:
                contents = f.read()
                matcher = char_to_search.findall(contents)
                for match in matcher:
                    print(file, ':', match)
    except Exception as e:
        print(e)


def recursive(char, files, dir_name):
    try:
        char_to_search = re.compile(r'.*{}.*'.format(char))
        for dir_path, dir_names, file_names in os.walk(dir_name):
            search_files = glob.glob(os.path.join(dir_path, files))
            for file in search_files:
                with open(file, 'r', encoding='utf-8') as f:
                    contents = f.read()
                    matcher = char_to_search.findall(contents)
                    for match in matcher:
                        print(file, ':', match)
    except Exception as e:
        print(e)


def ignore_case_sensitive(char, files, dir_name):
    try:
        char_to_search = re.compile(r'.*{}.*'.format(char), re.I)
        os.chdir(dir_name)
        search_files = glob.glob(files)
        for file in search_files:
            with open(file, 'r', encoding='utf-8') as f:
                contents = f.read()
                matcher = char_to_search.findall(contents)
                for match in matcher:
                    print(file, ':', match)
    except Exception as e:
        print(e)


def invert(char, files, dir_name):
    try:
        char_to_search = re.compile(r'.[^'+ char + '}].*')
        os.chdir(dir_name)
        search_files = glob.glob(files)
        for file in search_files:
            with open(file, 'r', encoding='utf-8') as f:
                contents = f.read()
                matcher = char_to_search.findall(contents)
                for match in matcher:
                    print(file, ':', match)
    except Exception as e:
        print(e)


def main():
    """ Main Function of the program """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("search", nargs='?', help="The character to search", type=str)
    parser.add_argument("files", nargs='?', help="The file pattern to search for", type=str)
    parser.add_argument("path", nargs='?', help="The directory path to search in", type=str)
    group.add_argument("-r", "--recursive", help="search the path to search in recursively", action="store_true")
    group.add_argument("-i", "--ignorecase", help="ignore case sensitivity", action="store_true")
    group.add_argument("-m", "--invertmatch", help="select non-matching lines", action="store_true")

    args = parser.parse_args()

    if args.recursive:
        recursive(args.search, args.files, args.path)
    elif args.ignorecase:
        ignore_case_sensitive(args.search, args.files, args.path)
    elif args.invertmatch:
        invert(args.search, args.files, args.path)
    else:
        grep(args.search, args.files, args.path)


if __name__ == '__main__':
    main()
