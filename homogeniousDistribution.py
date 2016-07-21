__author__ = 'ur5f'
import random

counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
counterHash = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lx = None
ly = None

for i in range(100000):

    x = random.randrange(11)
    y = random.randrange(1000) % 11
    while y == ly:
        y = random.randrange(1000) % 11

    if x == lx:
        counter[x] += 1
    lx = x

    if y == ly:
        counterHash[y] += 1
    ly = y


print(counter, sum(counter))
print(counterHash, sum(counterHash))
