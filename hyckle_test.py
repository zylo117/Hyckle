from hyckle import Hyckle

hk = Hyckle('helloworld.hyckle')

# use hyckle as a dict
hk['test_0'] = 1
hk['test_1'] = 2
hk['test_2'] = 3
hk['test_3'] = 4

hk.close()
