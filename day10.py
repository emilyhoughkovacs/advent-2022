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

        lines = [line.split(' ') for line in lines]

        x = 1
        cycle = 0
        cycleTimesX = list()

        for line in lines:
            if line[0] == 'noop':
                cycle += 1
                cycleTimesX.append(cycle * x)
            else:
                cycle += 1
                cycleTimesX.append(cycle * x)
                cycle += 1
                cycleTimesX.append(cycle * x)
                x += int(line[1])

        signalStrength = 0
        for i in range(19, len(cycleTimesX), 40):
            print(i, cycleTimesX[i])
            signalStrength += cycleTimesX[i]


        return signalStrength

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()