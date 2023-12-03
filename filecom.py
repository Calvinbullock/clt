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

    src_dir = directory_list(args.src)
    target_dir = directory_list(args.target)

    # TODO get the full path for each dir

    for src_file in src_dir:
        for target_file in target_dir:
            if target_file == src_file:
                #check last eddit date then replace target if older        
                src_file_info = os.stat(src_file) # TODO bug here
                src_file_last_mod = src_file_info.st_mtime
                
                target_file_info = os.stat(target_file) # TODO bug here
                target_file_last_mod = target_file_info.st_mtime

                if target_file_last_mod < src_file_last_mod:
                    #os.remove(file)
                    #os.copy(src_dir, target_dir)
                    print(f"{src_dir}, {target_dir}")


        # copy file to target
        print(f"{src_dir}, {target_dir}")
        #os.copy(src_dir, target_dir)


def directory_list(path):
    dir_files = []

    for x in os.listdir():
        dir_files.append(x)

    return dir_files

main()

