# print(dir())
# print(dir(__builtins__))
# for m in dir(__builtins__):
#     print(m)
import shelve
# print(dir())
# print()
#
# print(dir(shelve))
for obj in dir(shelve):
    if(obj[0]!='_'):
        print(obj)

import random
print(random.randint(0,100))