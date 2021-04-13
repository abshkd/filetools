#!/usr/bin/env python
#  Copyright (c) 2021.
#  Abhishek Dujari ab@singularity.sg
#

from system.Scanner import Cleanup

if __name__ == '__main__':
    start_dir = input("Enter a path to cleanup:")
    scanner = Cleanup(start_dir,
                      clean_dirs=[".svn"],  # also delete .svn directories
                      clean_files=[".lnk", ".url"])  # and shortcut file extension
    scanner.expand()
    print(f"Stats: {scanner.cleanup} items removed")
