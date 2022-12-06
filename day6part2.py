import sys
import os
import re

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputfile.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        startOfPacket = list()
        for line in lines:
            for i, char in enumerate(line):
                if i>=13 and len(set(line[i-13:i+1])) == 14:
                    print(i+1)
                    startOfPacket.append(i+1)
                    break
            print()

        return startOfPacket[-1]

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()