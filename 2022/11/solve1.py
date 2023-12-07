import math
import re
import functools
import sys, os
from ast import literal_eval
from icecream import ic
from collections import deque
from math import floor, prod

data = open('input').read().split('\n\n')

def _give_to_monkey(worry: int, n: int):
    global monkeys

    monkeys[n].recieve(worry)


class Monkey:
    def __init__(self, idx, starting_items, operation, test, if_true, if_false) -> None:
        self.id = idx
        self.items = deque(starting_items)
        self._operation = operation.lstrip(' ').rstrip(' ')[6:]
        self.divisible_by = int(test.lstrip(' ').rstrip(' ').split(' ')[-1])

        if_true = if_true.lstrip(' ').rstrip(' ')
        if_false = if_false.lstrip(' ').rstrip(' ')

        self.true_target = int(if_true.split(' ')[-1])
        self.false_target = int(if_false.split(' ')[-1])

        self.count_inspected = 0

    def operation(self, old):
        return eval(self._operation, {'old': old, __builtins__: {}})

    def _process_item(self, worry):
        worry = self.operation(worry) 
        worry = worry // 3
        if worry % self.divisible_by == 0:
            self.give_to_monkey(worry, self.true_target)
        else:
            self.give_to_monkey(worry, self.false_target)

        self.count_inspected += 1
    
    def _start_round(self):
        pass

    def _end_round(self):
        pass

    def run(self):
        self._start_round()

        while self.items:
            item = self.items.popleft()
            self._process_item(item)

        self._end_round()

    def recieve(self, worry):
        self.items.append(worry)
        pass
        
    def give_to_monkey(self, worry, n):
        _give_to_monkey(worry, n)

monkeys: list[Monkey] = []
for m in data:
    print(m)
    m = m.split('\n')
    idx = literal_eval(m[0][7: m[0].index(':')])
    starting_items = literal_eval(m[1][m[1].index(':')+1:])
    operation = m[2][m[2].index(':')+1:]
    test = m[3][m[3].index(':')+1:]
    if_true = m[4][m[4].index(':')+1:]
    if_false = m[5][m[5].index(':')+1:]

    starting_items = (starting_items,) if isinstance(starting_items, int) else starting_items
    monkeys.append(Monkey(idx, starting_items, operation, test, if_true, if_false))


for round in range(20):
    for monkey in monkeys:
        monkey.run()


inspect_cnt = [monkey.count_inspected for monkey in monkeys]
inspect_cnt.sort(reverse=True)
print(inspect_cnt[:2])
print(prod(inspect_cnt[:2]))