class LineObj:

    def __init__(self, s):
        s.rstrip()
        p = s.index('.')
        if p < 0:
            print(s)
        self.num = int(s[:p])
        self.txt = s[p + 2:]
        pass

    def __str__(self):
        return str(self.num) + ". " + self.txt

    def __repr__(self):
        return str(self.num) + ". " + self.txt
