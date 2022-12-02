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

        lines = [x.split(' ') for x in lines]

        def outcome(elf, you):
            if elf=='A':
                if you=='X':
                    return 3
                if you=='Y':
                    return 6
                if you=='Z':
                    return 0
            if elf=='B':
                if you=='X':
                    return 0
                if you=='Y':
                    return 3
                if you=='Z':
                    return 6
            if elf=='C':
                if you=='X':
                    return 6
                if you=='Y':
                    return 0
                if you=='Z':
                    return 3

        def score(you):
            if you=='X':
                return 1
            if you=='Y':
                return 2
            if you=='Z':
                return 3

        totalScore = 0
        for elfThrow, yourThrow in lines:
            totalScore += score(yourThrow) + outcome(elfThrow, yourThrow)

        return totalScore

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()