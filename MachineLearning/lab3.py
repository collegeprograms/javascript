import csv
import math

# Read CSV file
with open("play_tennis_dataset.csv") as f:
    data = list(csv.reader(f))

headers = data[0]
data = data[1:]


# Entropy
def entropy(data):
    yes = sum(row[-1] == "Yes" for row in data)
    no = len(data) - yes

    e = 0

    for x in [yes, no]:
        if x:
            p = x / len(data)
            e -= p * math.log2(p)

    return e


# Information Gain
def gain(data, col):
    e = entropy(data)

    for value in set(row[col] for row in data):
        subset = [row for row in data if row[col] == value]

        e -= len(subset) / len(data) * entropy(subset)

    return e


# Build ID3 tree
def id3(data, cols):

    # All examples have same class
    if all(row[-1] == data[0][-1] for row in data):
        return data[0][-1]

    # No attributes left
    if not cols:
        classes = [row[-1] for row in data]
        return max(set(classes), key=classes.count)

    # Select attribute with highest Information Gain
    best = max(cols, key=lambda c: gain(data, c))

    tree = {headers[best]: {}}

    # Create branches
    for value in set(row[best] for row in data):

        subset = [
            row for row in data
            if row[best] == value
        ]

        remaining_cols = [
            c for c in cols
            if c != best
        ]

        tree[headers[best]][value] = id3(
            subset,
            remaining_cols
        )

    return tree


# Build tree
tree = id3(
    data,
    list(range(len(headers) - 1))
)

print("Decision Tree:")
print(tree)


# Predict new sample
def predict(tree, sample):

    if not isinstance(tree, dict):
        return tree

    attribute = next(iter(tree))

    index = headers.index(attribute)

    value = sample[index]

    return predict(
        tree[attribute][value],
        sample
    )


# New sample
sample = [
    "Sunny",
    "Cool",
    "High",
    "Strong"
]

print("\nNew Sample:", sample)
print("Prediction:", predict(tree, sample))
