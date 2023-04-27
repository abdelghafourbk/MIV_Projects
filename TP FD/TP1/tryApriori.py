import pandas as pd
from csv import writer

data = pd.read_csv('transactions.csv')
head = data.columns
row, cols = len(data.axes[0]), len(data.axes[1])

min_sup = 2 / row


def sup(x, itemsets):
    global sup_x
    for i in range(cols):
        if itemsets[i] == x:
            sup_x = data.iloc[:, i].values
    return sup_x


def init_itemsets(k):
    itemsets = []
    head = data.columns
    while k <= len(head):
        # générér les itemsets
        itemsets.append(head[k])
    sup(head[k], itemsets)
    return itemsets


def conf(x, y, itemsets):
    xy = x + y
    return sup(xy, itemsets) / sup(x, itemsets)


def lift(x, y, min_conf, itemsets):
    xy = x + y
    lift = sup(xy, itemsets) / sup(x, itemsets) * sup(y, itemsets)
    if lift >= min_conf:
        return "regle solide"
    if lift == 1:
        return "regle forte"


def apriori():
    freq_itemsets = []
    k = 1
    while k <= len(head):
        itemsets = init_itemsets(k)
        k += 1
        sup(head[k], itemsets)

    return freq_itemsets


def row_sup():
    sup_row = []
    for i in range(row):
        p = data.iloc[:, i].values
        sub.append((sum(p) / row))
    return sup_row


print(head[0])
sub = row_sup()
print(sub)

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
