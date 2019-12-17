import argparse
import os
import sys


def replace():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', type=str)
    parser.add_argument('-o', '--old_dir', type=str)
    parser.add_argument('-new', '--new_dir', type=str)
    namespace = parser.parse_args(sys.argv[1:])
    name = str(namespace.name)
    old_path = str(namespace.old_dir)
    new_path = str(namespace.new_dir)

    if os.path.exists(old_path) == False:
        assert (old_path == False), "OLD FOLDER NOT FOUND"

    elif os.path.exists(old_path + '/' + name) == False:
        assert (os.path.exists(old_path) == False), "FILE NOT FOUND"

    elif os.path.exists(new_path) == False:
        os.replace(old_path + '/' + name, str(os.mkdir(new_path)) + '/' + name)

    else:
        os.replace(old_path + '/' + name, new_path + '/' + name)

    return parser


if __name__ == '__main__':
    replace()
    try:
        replace()
    except AssertionError as a_error:
        print(a_error)
