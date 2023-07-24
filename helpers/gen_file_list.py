#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Generate File Listing

"Generate File Listing"

# Programmed by CoolCat467

__title__ = "Generate File List"
__author__ = "CoolCat467"
__version__ = "0.1.0"
__ver_major__ = 0
__ver_minor__ = 1
__ver_patch__ = 0

import json
import os
from typing import Any, Container


def get_file_list(
    root: str, ignore_paths: Container | None = None
) -> dict[str, dict | list[str]]:
    "Return file list dictionary"
    if ignore_paths is None:
        ignore: Container = set()
    else:
        ignore = ignore_paths

    root_len = len(root) + len(os.path.sep)
    dirs: dict[str, Any] = {}

    for dirpath, _dirnames, filenames in os.walk(root):
        filenames = [f for f in filenames if f not in ignore]
        if not filenames:
            continue
        entry = dirpath[root_len:]

        follow = entry.split(os.path.sep)
        if len(follow) > 1:
            if follow[0] not in dirs:
                dirs[follow[0]] = {}
            part = dirs[follow[0]]
            for link in follow[1:]:
                if link not in part:
                    part[link] = {}
                part = part[link]
            part[""] = filenames
        elif entry:
            dirs[entry] = {"": filenames}
        else:
            dirs[entry] = filenames
    return dirs


def run() -> None:
    "Generate file listing for update module."
    root, this = os.path.split(__file__)
    ignore = (this,)

    dirs = get_file_list(root, ignore)

    # print(dirs)
    print(json.dumps(dirs, indent=2))

    # with open(os.path.join(root, 'files.json'), 'w', encoding='utf-8') as fp:
    #     json.dump(dirs, fp, indent=2)
    # print('\nData written.')


if __name__ == "__main__":
    print(f"{__title__} v{__version__}\nProgrammed by {__author__}.")
    run()
