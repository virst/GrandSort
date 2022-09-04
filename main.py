import os
import time
from generator import make_file
from sorter import split_file, merge_files

size = 10_000
part = int(size/10)

start_time = time.time()
fn = make_file(size)
print("make time %s" % (time.time() - start_time))

start_time = time.time()
fls = split_file(fn, part)
print("split time %s" % (time.time() - start_time))

for f in fls:
    print(f)

start_time = time.time()
rez = merge_files(fn, fls)
print("merge time %s" % (time.time() - start_time))

print("rez = " + rez)

print("clear")
# os.remove(fn)
for f in fls:
    os.remove(f)
print("done")
