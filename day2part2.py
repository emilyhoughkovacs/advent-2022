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
                    return 0 + 3
                if you=='Y':
                    return 3 + 1
                if you=='Z':
                    return 6 + 2
            if elf=='B':
                if you=='X':
                    return 0 + 1
                if you=='Y':
                    return 3 + 2
                if you=='Z':
                    return 6 + 3
            if elf=='C':
                if you=='X':
                    return 0 + 2
                if you=='Y':
                    return 3 + 3
                if you=='Z':
                    return 6 + 1

        totalScore = 0
        for elfThrow, yourThrow in lines:
            totalScore += outcome(elfThrow, yourThrow)

        return totalScore

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()