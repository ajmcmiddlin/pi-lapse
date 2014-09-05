#!/usr/bin/env python

import sys
import glob
import os

src_dir = sys.argv[1]
dest_dir = sys.argv[2]

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

files = sorted(glob.glob(src_dir + "/*.jpg"))

for i, f in enumerate(files):
    os.symlink(f, os.path.join(dest_dir, "%05d.jpg" % (i + 1)))

