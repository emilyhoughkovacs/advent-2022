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
        lines = [[line[0], int(line[1])] for line in lines]

        head = [0, 0]
        pos1 = [0, 0]
        pos2 = [0, 0]
        pos3 = [0, 0]
        pos4 = [0, 0]
        pos5 = [0, 0]
        pos6 = [0, 0]
        pos7 = [0, 0]
        pos8 = [0, 0]
        tail = [0, 0]

        def moveTail(h=head, t=tail):
            horizontalDiff = h[0]-t[0]
            verticalDiff = h[1]-t[1]

            if abs(horizontalDiff) <= 1 and abs(verticalDiff) <= 1 or abs(horizontalDiff) <= 1 and abs(verticalDiff) <= 1:
                return t

            elif verticalDiff == 0:
                if horizontalDiff == 2:
                    return [t[0]+1, t[1]]
                elif horizontalDiff == -2:
                    return [t[0]-1, t[1]]

            elif horizontalDiff == 0:
                if verticalDiff == 2:
                    return [t[0], t[1]+1]
                elif verticalDiff == -2:
                    return [t[0], t[1]-1]

            elif horizontalDiff >= 1 and verticalDiff >= 1:
                return [t[0]+1, t[1]+1]

            elif horizontalDiff >= 1 and verticalDiff <= -1:
                return [t[0]+1, t[1]-1]

            elif horizontalDiff <= -1 and verticalDiff >= 1:
                return [t[0]-1, t[1]+1]

            elif horizontalDiff <= -1 and verticalDiff <= -1:
                return [t[0]-1, t[1]-1]

        # print(moveTail([2,1], [1,1]))
        # print(moveTail([1,2], [2,1]))
        # print(moveTail([1,1], [1,1]))
        # print(moveTail([3,1], [1,1]))
        # print(moveTail([1,2], [1,3]))
        # print(moveTail([1,1], [1,3]))
        # print(moveTail([2,3], [1,1]))
        # print(moveTail([3,2], [1,1]))

        tailLocations = [tail]

        for [direction, amount] in lines:
            for _ in range(amount):
                if direction == 'R':
                    head = [head[0]+1, head[1]]
                    pos1 = moveTail(head, pos1)
                    pos2 = moveTail(pos1, pos2)
                    pos3 = moveTail(pos2, pos3)
                    pos4 = moveTail(pos3, pos4)
                    pos5 = moveTail(pos4, pos5)
                    pos6 = moveTail(pos5, pos6)
                    pos7 = moveTail(pos6, pos7)
                    pos8 = moveTail(pos7, pos8)
                    tail = moveTail(pos8, tail)
                    tailLocations.append(tail)
                if direction == 'U':
                    head = [head[0], head[1]+1]
                    pos1 = moveTail(head, pos1)
                    pos2 = moveTail(pos1, pos2)
                    pos3 = moveTail(pos2, pos3)
                    pos4 = moveTail(pos3, pos4)
                    pos5 = moveTail(pos4, pos5)
                    pos6 = moveTail(pos5, pos6)
                    pos7 = moveTail(pos6, pos7)
                    pos8 = moveTail(pos7, pos8)
                    tail = moveTail(pos8, tail)
                    tailLocations.append(tail)
                if direction == 'L':
                    head = [head[0]-1, head[1]]
                    pos1 = moveTail(head, pos1)
                    pos2 = moveTail(pos1, pos2)
                    pos3 = moveTail(pos2, pos3)
                    pos4 = moveTail(pos3, pos4)
                    pos5 = moveTail(pos4, pos5)
                    pos6 = moveTail(pos5, pos6)
                    pos7 = moveTail(pos6, pos7)
                    pos8 = moveTail(pos7, pos8)
                    tail = moveTail(pos8, tail)
                    tailLocations.append(tail)
                if direction == 'D':
                    head = [head[0], head[1]-1]
                    pos1 = moveTail(head, pos1)
                    pos2 = moveTail(pos1, pos2)
                    pos3 = moveTail(pos2, pos3)
                    pos4 = moveTail(pos3, pos4)
                    pos5 = moveTail(pos4, pos5)
                    pos6 = moveTail(pos5, pos6)
                    pos7 = moveTail(pos6, pos7)
                    pos8 = moveTail(pos7, pos8)
                    tail = moveTail(pos8, tail)
                    tailLocations.append(tail)
            # print(tailLocations)


        return len(set(tuple(location) for location in tailLocations))

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()