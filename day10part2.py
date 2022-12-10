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
        lights = list()

        for line in lines:
            if line[0] == 'noop':
                if abs(x-cycle%40) <= 1:
                    lights.append('#')
                else:
                    lights.append('.')
                cycle += 1
            else:
                if abs(x-cycle%40) <= 1:
                    lights.append('#')
                else:
                    lights.append('.')
                cycle += 1
                if abs(x-cycle%40) <= 1:
                    lights.append('#')
                else:
                    lights.append('.')
                cycle += 1
                x += int(line[1])

        for i in range(0, len(lights)+40, 40):
            print(''.join(lights[i:i+40]))

        return lights

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()