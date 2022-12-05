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

        for i, line in enumerate(lines):
            if line[0:2] == ' 1':
                num_crates = int(line.strip().split(' ')[-1])
                crate_rows = lines[0:i]
                instructions = lines[i+2:]
                break

        crates = list()
        for line in crate_rows[::-1]:
            res = re.split(' \[|\] |\[|\]', line)
            res = [x for x in res if x!='']
            myList = list()
            for x in res:
                if x.strip()!='' or x=='   ':
                    myList.append(x)
                else:
                    for _ in range(int(len(x)/len('   '))):
                        myList.append('   ')
            crates.append(myList)
            print(myList)

        crates = [[crates[j][i] for j in range(len(crates))] for i in range(len(crates[0]))]

        print()

        crates = [[x for x in row if x.strip()!=''] for row in crates]
        for row in crates:
            print(row)

        print()

        parsed_instructions = list()
        for line in instructions:
            res = re.split('move | from | to ', line)
            res = [int(x) for x in res if x!='']
            parsed_instructions.append([res[0], res[1]-1, res[2]-1])

        for num, start, finish in parsed_instructions:
            for _ in range(num):
                move = crates[start].pop()
                crates[finish].append(move)

        return ''.join([stack[-1] for stack in crates])

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()