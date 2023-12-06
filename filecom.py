import os
import argparse
import shutil

# For my refance this tool is a inferier "rsync" / "diff"

# Take in a source and a target check every file in the target agenst the src.
#       Compare names and the modifiyed date to check if the files have been moded
#       since last time. or if the file isent in the target dir but is in the source.


# ______MAIN TODO PATH is hardcoded not changeable for each file...

# TODO get the full path for each dir
PATH = "/home/calvin/Documents/clt/"

def main():
    # TODO move parser to other func
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--src", type=str, help="The name of the directory you copy from."
    )
    parser.add_argument("--target", type=str, help="The directory you want to copy to.")
    args = parser.parse_args()

    src_dir_path = PATH + args.src
    target_dir_path = PATH + args.target

    src_dir_ls = os.listdir(src_dir_path)
    target_dir_ls = os.listdir(target_dir_path)

    # FOR DEBUGING
    # print("src-", src_dir_ls)
    # print("tar-", target_dir_ls)

    for src_file in src_dir_ls:
        if len(target_dir_ls) < 1:
            shutil.copyfile(f"{src_dir_path}/{src_file}", f"{target_dir_path}/{src_file}")

        else:
            for target_file in target_dir_ls:
                if target_file == src_file:
                    # check last eddit date then replace target if older
                    src_file_info = os.stat(src_dir_path + "/" + src_file)
                    src_file_last_mod = src_file_info.st_mtime

                    target_file_info = os.stat(target_dir_path + "/" + target_file)
                    target_file_last_mod = target_file_info.st_mtime

                    if target_file_last_mod < src_file_last_mod:
                        os.remove(f"{target_dir_path}/{target_file}")
                        shutil.copyfile(f"{src_dir_path}/{src_file}", f"{target_dir_path}/{src_file}")

                else:
                    shutil.copyfile(f"{src_dir_path}/{src_file}", f"{target_dir_path}/{src_file}")


main()
