from NameGenerator import gen_name
from NumGenerator import gen_num
import random

file = open('Data.txt', 'w')

for i in range(10000):
    rand = random.randint(0, 9)
    if rand <= 4:
        file.write("%d:'%s'\n" % (i + 1, gen_name()))
    elif rand <= 8:
        file.write("%d:%d\n" % (i + 1, gen_num()))
    else:
        file.write("%d:%s\n" % (i + 1, 'Null'))
    if i % 10000 == 0:
        print(int(i / 10000 + 1))

file.close()
