from drawman import *
from time import sleep
def f(x):
    return x*x

pen_down()
for x in range(-11,11):
    to_point(x,f(x))
pen_up()
sleep(5)
