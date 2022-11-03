# Copyright Amir Zedah
import re


VERSION = "1.2.0"


def is_release_version():
    return bool(re.match(r"^\d+\.\d+\.\d+$", VERSION))
