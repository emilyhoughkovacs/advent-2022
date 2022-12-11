import sys
import os
import re
import math

class Solution(object):
    def __init__(self):
        self.args = [arg for arg in sys.argv[1:]]

    def solution(self, args):

        # uses first command line arg if exists else inputfile.txt
        file = args[0] if args and os.path.isfile(args[0]) else 'inputfile.txt'
        f = open(file, 'r')
        lines = f.read()
        f.close()

        lines = lines.split('\n\n')
        lines = [line.split('\n') for line in lines]
        tests = list()

        items = list()
        operations = list()
        for line in lines:
            monkeyItems = line[1].split(': ')[1]
            monkeyItems = monkeyItems.split(', ')
            monkeyItems = [int(x) for x in monkeyItems]
            items.append(monkeyItems)
            operation = line[2].split(' = ')[1]
            operation = operation.split(' ')
            operations.append(operation[1:3])
            test = [int(l.split(' ')[-1]) for l in line[3:6]]
            tests.append(test)
        
        operations = [[op[0], int(op[1])] if op[1]!='old' else op for op in operations]
        for i, op in enumerate(operations):
            if op[1]=='old':
                if op[0]=='+':
                    operations[i] = ['*', 2]
                elif op[0]=='*':
                    operations[i] = ['**', 2]
        
        inspected = [0 for _ in range(len(items))]

        def operate(item, monkeyNum, operations=operations,):
            if operations[monkeyNum][0] == '+':
                item += operations[monkeyNum][1]
            elif operations[monkeyNum][0] == '*':
                item = item * operations[monkeyNum][1]
            elif operations[monkeyNum][0] == '**':
                item = item ** operations[monkeyNum][1]
            return math.floor(item/3)

        for _ in range(20):
            for num, monkey in enumerate(items):
                while len(monkey) > 0:
                    i = items[num].pop(0)
                    i = operate(i, num)
                    if i%tests[num][0]==0:
                        items[tests[num][1]].append(i)
                    else:
                        items[tests[num][2]].append(i)
                    inspected[num] += 1


        inspected.sort(reverse=True)

        return inspected[0]*inspected[1]

def main():
    s = Solution()
    print(s.solution(s.args))

if __name__ == '__main__':
    main()