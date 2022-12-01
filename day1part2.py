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

        lines = ','.join(lines)

        lines = lines.split(',,')

        lines = [x.split(',') for x in lines]

        calories = list()

        for x in lines:
            calories.append(sum([int(y) for y in x]))

        calories = sorted(calories, reverse=True)

        return sum(calories[0:3])

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()