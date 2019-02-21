############################################################
#### Open given files and compare for overlapping numbers ##
#### And return a sorted list                             ##
#### Made by maevus                                       ##
#### Feb 21 2019                                          ##
############################################################

import argparse

class Overlap():

    def __init__(self, file1, file2):
        
        self.lines1 = file1.read().splitlines()
        self.lines2 = file2.read().splitlines()

        match = self.match(self.lines1, self.lines2)

        print (sorted(self.strToInt(match)))
        
    def match(self,a,b):
        return set(a).intersection(b)

    def strToInt(self, a):
        return list(map(int,a))

def main():
    print('Initating...')
    parser = argparse.ArgumentParser(usage='python overlap.py filename filename',
                                     description="Compares two files for overlapping numbers")
    parser.add_argument('file1', type=argparse.FileType('r'))
    parser.add_argument('file2', type=argparse.FileType('r'))
    args = parser.parse_args()

    Overlap(args.file1, args.file2)

main()
