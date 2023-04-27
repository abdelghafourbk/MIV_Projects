from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
import time
import random

dict_ = {
    'A': [1, 0, 1, 0, 0],
    'B': [0, 1, 1, 1, 1],
    'C': [1, 1, 0, 0, 0],
    'D': [1, 0, 0, 1, 1],
    'E': [0, 1, 1, 0, 1]

}


df = pd.DataFrame(dict_)


apriori_time = []
close_time = []
data_size = []

for i in range(10):
    # add data
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res
    res = [random.randrange(0, 2, 1) for p in range(5)]
    df.loc[len(df.index)] = res

    # pretraitement taena
    te = TransactionEncoder()
    te_ary = te.fit(df).transform(df)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    # Measure the time taken by the Apriori algorithm
    start_time = time.time()
    frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)
    apriori_time.append(time.time() - start_time)

    # Measure the time taken by the Close algorithm
    start_time = time.time()
    frequent_itemsets = fpgrowth(df, min_support=0.4, use_colnames=True)
    close_time.append(time.time() - start_time)

    row, cols = len(df.axes[0]), len(df.axes[1])
    data_size.append(row * cols)

from matplotlib import pyplot as plt

plt.plot(data_size, apriori_time, label='Apriori')
plt.plot(data_size, close_time, label='Close')
plt.legend()
plt.ylabel("Time (s)")
plt.xlabel("Data size")
plt.show()
