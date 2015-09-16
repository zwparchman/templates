#!/usr/bin/python
from collections import defaultdict
def words_to_dict( words, header):
    ret={}
    for a,b in zip(words,header):
        ret[b]=[a]
    return ret


def words(s): return s.split()

p=[10**x for x in range(20)]
def toNumber(s):
    try:
        if( int(s) in p ):
            return int(s)
    except Exception as e:
        pass
    v = float(s)
    if v == 0 :
        v=1
    return v

def byFileName( fname ):
    with file(fname,"r") as f:
        lines = f.readlines()
        lines = lines[3:]
        #first line contains columns
        header = words(lines[0].lower())
        #remove header line
        lines = lines[1:]

        wl = map( words , lines )
        wl = map( lambda x: map( toNumber, x), wl)

        ret = defaultdict(list)
        for l in wl:
            for a,b in zip(header,l):
                ret[a].append(b)

        return ret

if __name__ == "__main__":
    print byFileName("./data.csv")
