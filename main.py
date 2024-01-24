import argparse
import os

import all_in_one_md

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="All In One Markdown",
        description="Merge all markdown files found in the given "
        "directory into one markdown file and convert it into a pdf file.",
    )
    parser.add_argument(
        "working_directory",
        default=os.getcwd(),
        help="The directory to search in. (Default: current working directory)",
    )
    parser.add_argument(
        "output_filepath",
        default="all_in_one.pdf",
        help="The output pdf file path, either absolute or relative. "
        "The markdown file merged into is of the same path but with suffix `.md`. "
        "(Default: all_in_one.pdf)",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Whether to search the directory recursively. (Default: False)",
    )
    parser.add_argument(
        "-e",
        "--encoding",
        default="utf-8",
        help="The encoding for both reading and writing. (Default: utf-8)",
    )

    config = parser.parse_args()
    gb = all_in_one_md.GitBook(**vars(config))
    gb.merge_and_convert()
