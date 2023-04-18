import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import tkinter as tk

def generate_rules():
    data = textarea.get("1.0", "end-1c").split("\n")
    data = list(filter(None, data))
    te = TransactionEncoder()
    te_ary = te.fit(data).transform(data)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    min_support = float(min_support_input.get())

    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)

    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
    result_textarea.delete("1.0", tk.END)
    result_textarea.insert(tk.END, "Frequent Itemsets:\n")
    result_textarea.insert(tk.END, str(frequent_itemsets) + "\n\n")
    result_textarea.insert(tk.END, "Association Rules:\n")
    result_textarea.insert(tk.END, str(rules))


# GUI 
root = tk.Tk()
root.title("Apriori Algorithm")

data_label = tk.Label(root, text="Transaction Data:")
data_label.pack()
textarea = tk.Text(root, height=10, width=50)
textarea.pack()

min_support_label = tk.Label(root, text="Minimum Support:")
min_support_label.pack()
min_support_input = tk.Entry(root)
min_support_input.pack()

generate_button = tk.Button(root, text="Generate Rules", command=generate_rules)
generate_button.pack()
result_label = tk.Label(root, text="Results:")
result_label.pack()
result_textarea = tk.Text(root, height=10, width=50)
result_textarea.pack()

root.mainloop()
