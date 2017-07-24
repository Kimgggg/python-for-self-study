#!/usr/bin/env python

import os
import sys
import shutil

old_version = sys.argv[1]
new_version = sys.argv[2]
# old_version = '1.1.0'
# new_version = '9.9.0'

print 'version  --- ',old_version,new_version
def changeName(old,new,filename):
    old_version = old
    new_version = new
    tail = '.hjson'
    old_name = filename
    new_name = tail
    t_pos = old_name.rindex('_') + 1
    l_pos = old_name.index(tail)
    file_version = old_name[t_pos:l_pos]
    chanel_name = old_name[:t_pos]
    if file_version == old_version :
        new_name = chanel_name + new_version + tail
        return new_name
    else:
        return None

def main():
    cur_path = os.path.dirname(__file__)
    version_path = os.path.join(cur_path, 'scard_versions')
    for parent, dirs, files in os.walk(version_path):
        for f in files:
            new_name = changeName(old_version,new_version,f)
            if new_name:
                old_path_name = os.path.join(version_path, f)
                new_path_name = os.path.join(version_path, new_name)
                shutil.copy2(old_path_name, new_path_name)

if __name__ == '__main__':
    main()