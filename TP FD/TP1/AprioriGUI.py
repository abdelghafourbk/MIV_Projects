import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import tkinter as tk


# Function to generate frequent itemsets and association rules
def generate_rules():
    # Get transaction data from textarea
    data = textarea.get("1.0", "end-1c").split("\n")
    # Remove any empty lines from data
    data = list(filter(None, data))
    # Convert transaction data to one-hot encoding
    te = TransactionEncoder()
    te_ary = te.fit(data).transform(data)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    # Get minimum support threshold from input
    min_support = float(min_support_input.get())
    min_confidence = float(min_confidence_input.get())
    # Generate frequent itemsets
    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
    # Output results to result_textarea
    result_textarea.delete("1.0", tk.END)
    result_textarea.insert(tk.END, "Frequent Itemsets:\n")
    result_textarea.insert(tk.END, str(frequent_itemsets) + "\n\n")
    result_textarea.insert(tk.END, "Association Rules:\n")
    result_textarea.insert(tk.END, str(rules))

    print("Frequent Itemsets:\n")
    print(str(frequent_itemsets) + "\n\n")
    print("Association Rules:\n")
    print(str(rules))


# Create GUI window
root = tk.Tk()
root.title("Apriori Algorithm & Association Rule Mining")

# Create label and textarea for transaction data
data_label = tk.Label(root, text="Transaction Data:")
data_label.pack()
textarea = tk.Text(root, height=10, width=50)
textarea.pack()

# Create label and input for minimum support threshold
min_support_label = tk.Label(root, text="Minimum Support:")
min_support_label.pack()
min_support_input = tk.Entry(root)
min_support_input.pack()

# Create label and input for minimum support threshold
min_confidence_label = tk.Label(root, text="Minimum Confidence:")
min_confidence_label.pack()
min_confidence_input = tk.Entry(root)
min_confidence_input.pack()

# Create button to generate rules
generate_button = tk.Button(root, text="Generate Rules", command=generate_rules)
generate_button.pack()

# Create label and textarea for results
result_label = tk.Label(root, text="Results:")
result_label.pack()
result_textarea = tk.Text(root, height=10, width=50)
result_textarea.pack()

# Run GUI window
root.mainloop()
