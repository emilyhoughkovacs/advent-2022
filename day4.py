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

        fullyContained = 0
        for sections in elves:
            if sections[0][0] <= sections[1][0] and sections[0][1] >= sections[1][1] or sections[0][0] >= sections[1][0] and sections[0][1] <= sections[1][1]:
                fullyContained += 1


        return fullyContained

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()