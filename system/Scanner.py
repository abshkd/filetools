#  Copyright (c) 2021.
#  Abhishek Dujari ab@singularity.sg
#

import os
import shutil


class Cleanup:
    def __init__(self, start_dir, clean_dirs=None, clean_files=None):
        self.start = start_dir
        self.clean_dirs = clean_dirs
        self.clean_files = clean_files
        self.cleanup = 0

    def expand(self, path=None):
        if not path:
            path = self.start
        with os.scandir(path) as it:
            is_empty = True
            for entry in it:
                is_empty = False
                if entry.is_dir():
                    if entry.name in self.clean_dirs:
                        shutil.rmtree(entry)
                        print(f"removing {path}{entry.name}")
                        self.cleanup += 1
                    else:
                        self.expand(entry)
                else:
                    st = os.stat(entry)
                    if st.st_size == 0 or os.path.splitext(entry.name)[-1] in self.clean_files:
                        try:
                            os.remove(entry)
                            print(f"removing {path}{entry.name}")
                            self.cleanup += 1
                        except PermissionError:
                            pass
            if is_empty:
                os.removedirs(path)
                print(f"removing {path.name}")
                self.cleanup += 1
        return True
