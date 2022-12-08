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

        x = 1
        y = 2

        print(lines[x][y])
        scores = list()

        for x in range(1, len(lines)-1):
            for y in range(1, len(lines[0])-1):
                left = lines[x][0:y][::-1]
                right = lines[x][y+1:]
                top = [line[y] for line in lines[0:x]][::-1]
                bottom = [line[y] for line in lines[x+1:]]
                directions = [left, right, top, bottom]
                print(top)

                scenicScore = 1
                for direction in directions:
                    if lines[x][y] > max(direction):
                        scenicScore = scenicScore * len(direction)
                    else:
                        directionScore = 1
                        for i, a in enumerate(direction):
                            if a >= lines[x][y]:
                                directionScore += i
                                break
                        scenicScore = scenicScore * directionScore
                scores.append(scenicScore)

        return max(scores)

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()