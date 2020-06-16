# Author: Zylo117
import msgpack

from hyckle import Hyckle

# create or reload a hyckle file.
# This will create a new hyckle file if not exists or reload a existed hyckle file.
hk = Hyckle('helloworld.hyckle')

# create a super complex variable
import numpy as np
import time


class Dog:
    def __init__(self):
        self.weight = 50
        self.brain = np.random.randint(0, 99,
                                       [np.random.randint(0, 99), np.random.randint(0, 99), np.random.randint(0, 99)])
        self.stamina = 50

    def sleep(self):
        for i in range(5):
            time.sleep(1)
            self.stamina += 1
            print(self.stamina)


# use hyckle as a dict
hk['test_0'] = 1
hk['test_1'] = [2]
hk['test_2'] = {3}
hk['test_3'] = {4: ['5', 6]}

# use hyckle as a list
hk.append(7)
hk.append('8')

# check the length of hyckle
length = len(hk)
print('total length', length)

# use hyckle as a iterable object
print('current content:')
for obj in hk:
    print(obj)

# get certain object by key: str
obj_0 = hk.get('test_0')
print('item of test_0:')
print(obj_0)

# or using getitem method
obj_1 = hk['test_1']
print('item of test_1:')
print(obj_1)

# get certain object by index: int
obj_2 = hk[3]
print('third item:')
print(obj_2)

# get certain items by slice
objs = hk[2:5]
print('items from second to fifth:')
print(objs)

# remove key in hyckle
print('current keys:')
print(hk.keys)
hk.remove('test_0')
hk.remove('test_1')
print('current keys after removal:')
print(hk.keys)

# magic time
print('time to try on some complex variable:')

hk['dog'] = Dog()
print('retrieve variable from hyckle:')
dog = hk['dog']
print('check this variable\'s class-variable:')
print(dog.brain.shape)
print('use this variable\'s class-method:')
dog.sleep()

# flush to disk.
# Normally hyckle will auto-flush to disk every K item adding (K = buffersize)
hk.flush()

# close a hyckle file.
# After final reading/writing hyckle, you should close it to ensure data integrity.
hk.close()

# custom_dumps_func and custom_loads_func
hk = Hyckle('helloworld.hyckle', custom_dumps_func=msgpack.packb,
            custom_loads_func=msgpack.unpackb)
hk[1] = '123'
a = hk['1']
hk.close()
