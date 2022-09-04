import os

from line import LineObj


class FileReader:

    def __init__(self, fn):
        self.cur_line = None
        self.f = open(fn)
        self.end = False

    def next(self):
        if self.end:
            return
        s = self.f.readline()
        s = s.rstrip()
        if s == '':
            self.cur_line = None
            self.end = True
            self.f.close()
        else:
            self.cur_line = LineObj(s)


def merge_files(fn, fls):
    fp = os.path.splitext(fn)
    fn = fp[0] + "_rez" + fp[1]
    readers = []
    for f in fls:
        rd = FileReader(f)
        rd.next()
        readers.append(rd)

    f = open(fn, 'w')
    while len(readers) > 0:
        readers = sorted(readers, key=lambda x: (x.cur_line.txt, x.cur_line.num))
        f.write(str(readers[0].cur_line) + '\n')
        readers[0].next()
        if readers[0].end:
            readers.remove(readers[0])
    f.close()
    return fn


def save_file(fnb, tmp, files):
    num = len(files)
    tmp = sorted(tmp, key=lambda x: (x.txt, x.num))
    fp = os.path.splitext(fnb)
    fn = fp[0] + "_" + str(num+1) + fp[1]
    files.append(fn)
    f = open(fn, 'w')
    for line in tmp:
        f.write(str(line)+ '\n')
    f.close()


def split_file(fn, part_size):
    files = []
    tmp = []
    f = open(fn)
    for line in f:
        if len(tmp) == part_size:
            save_file(fn, tmp, files)
            tmp = []
        if line == "":
            continue
        lo = LineObj(line)
        tmp.append(lo)
    if len(tmp) > 0:
        save_file(fn, tmp, files)
    f.close()
    return files
