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

        priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        prioDict = {c:i+1 for i, c in enumerate(priorities)}

        items = list()

        for line in lines:
            halfway = int(len(line)/2)
            firstHalf = line[0:halfway]
            secondHalf = line[halfway:]

            for c in firstHalf:
                if c in secondHalf:
                    items.append(c)
                    break

        total = 0
        for item in items:
            total += prioDict[item]

        return total

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()