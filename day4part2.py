import sys
import os

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputfile.txt'
        f = open(file, 'r')
        lines = f.read().splitlines()
        f.close()

        lines = [line.split(',') for line in lines]

        elves = list()
        for line in lines:
            line = [x.split('-') for x in line]
            elves.append(line)

        elves = [[[int(x) for x in instructions] for instructions in pairs] for pairs in elves]

        overlap = 0
        for sections in elves:
            if sections[0][0] <= sections[1][0] and sections[1][0] <= sections[0][1] or sections[1][0] <= sections[0][1] and sections[1][1] >= sections[0][0]:
                overlap += 1


        return overlap

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()