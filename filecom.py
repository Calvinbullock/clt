import os
import argparse

# For my refance this tool is a inferier "rsync" / "diff"

# TODO take in a sorce and a target check every file in the target agenst the src. 
#       Compare names and the modifiyed date to check if the files have been moded
#       since last time. or if the file isent in the target dir but is in the source.


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, help='The name of the directory you copy from.')
    parser.add_argument('--target', type=str, help='The directory you want to copy to.')
    args = parser.parse_args()

    print('Hello, {}!'.format(args.src, args.target))


def directory_list(path):
    dir_files = []

    for x in os.listdir():
        dir_files.append(x)

    return dir_files
