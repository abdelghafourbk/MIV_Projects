import pandas as pd
import definitions

data = pd.read_csv('TPClose/transactions')

minsupport = int(input("enter Minsup: "))
definitions.close(minsupport, data)
