############################################################
#### Display specified names in a file                    ##
#### Made by maevus                                       ##
#### Feb 21 2019                                          ##
############################################################

import argparse


class Select():

        def __init__(self, file, linenums):

             self.linenums = linenums
             self.names = file.read().splitlines()
             self.printLine(self.names, self.linenums)

        def printLine(self, lines, nums):

                try:
                     print(lines[nums])
                except:
                        for i in nums:
                              if i <= len(lines):
                                    print(lines[i])
                finally:
                        print ("Line number not found, please select a line between 0 and " + str(len(lines)))


def main():
    print ('Initiating...')
    parser = argparse.ArgumentParser(usage='python select.py filename')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--line',  metavar='N', dest='linenums', type=int, nargs='+', default=0)
    
    args = parser.parse_args()

    try:
        file = open('names.txt', 'r')
        Select(args.file, args.linenums)
    except IOError: 
        print ('File not found' + ' ' + str(IOError))
    

main()
