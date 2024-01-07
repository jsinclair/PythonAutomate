import time
import sys

indent = 0
mod = 1
while True:
    print(' ' * indent, '********')
    indent += mod
    time.sleep(0.05)

    if indent == 5:
        mod = -1
    elif indent == 0:
        mod = 1