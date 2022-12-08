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

        lines = [[int(x) for x in line] for line in lines]

        visible = len(lines[0])*2 + len(lines)*2 - 4

        for x in range(1, len(lines)-1):
            for y in range(1, len(lines[0])-1):
                left = lines[x][0:y]
                right = lines[x][y+1:]
                top = [line[y] for line in lines[0:x]]
                bottom = [line[y] for line in lines[x+1:]]
                if lines[x][y] > max(left) or lines[x][y] > max(right) or lines[x][y] > max(top) or lines[x][y] > max(bottom):
                    visible += 1

        return visible

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()