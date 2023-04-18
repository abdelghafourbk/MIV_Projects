import pandas as pd
from csv import writer

data = pd.read_csv('TP1/TP1/transactions')
head = data.columns
print(head)
row, cols = len(data.axes[0]), len(data.axes[1])
sub = []
for i in range(row):
    p = data.iloc[:, i].values
    sub.append((sum(p) / row))

print(sub)
min_sup = 2 / row
new_head = []
kept_index = []
infrequent = []
for i in range(len(head)):
    if sub[i] > min_sup:
        new_head.append(head[i])
        kept_index.append(i)
    else:
        infrequent.append(head[i])

print(new_head)
print(kept_index)

new_new_head = []
new_subs = []
for conc in range(len(new_head)):
    if conc < len(new_head) - 1:
        for j in range(conc + 1, len(new_head)):
            new_new_head.append(new_head[conc] + new_head[j])
            new_subs.append(sub[kept_index[conc]] + sub[kept_index[j]])

print(new_new_head)
print(new_subs)
