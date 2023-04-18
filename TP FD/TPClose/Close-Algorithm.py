import pandas as pd
import definitions

data = [['A', 'B', 'C', 'D', 'E'],
        [1, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1]]

# minsupport = int(input("enter Minsup: "))
definitions.close(2, data)
