#!/usr/bin/env python
#  Copyright (c) 2021.
#  Abhishek Dujari ab@singularity.sg
#

from system.Scanner import Cleanup

if __name__ == '__main__':
    start_dir = input("Enter a path to cleanup:")
    scanner = Cleanup(start_dir, [".svn"], [".lnk", ".url"])  # also delete .svn directories and shortcut files
    scanner.expand()
    print(f"Stats: {scanner.cleanup} items removed")
