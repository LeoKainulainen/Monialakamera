"""
codereuse
"""
import os
import time

# class codereuse:
def __init__(*args):
    self.args = args
def folderexist(*args):
    print("3", args[0])
    print("tadaa", args)
    for fname in args:
        if not os.path.exists(fname):
            os.makedirs(fname)

def exists(path):
    print(type(path),path)
    "Check if path (image) exists"
    try:
        print(path % 0)
        st = os.stat(path % 0)
    except os.error:
        return False
    print("Image roll already exists in" + path % 0)
    return True
