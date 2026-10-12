import csv
import math
from collections import Counter

with open("play_tennis_lab3.csv", newline="") as file:
    data = list(csv.DictReader(file))

TARGET = "PlayTennis"
ATTRIBUTES = ["Outlook", "Temperature", "Humidity", "Wind"]


def entropy(rows):
    counts = Counter(row[TARGET] for row in rows)
    total = len(rows)
    return -sum((n / total) * math.log2(n / total)
                for n in counts.values())


def information_gain(rows, attribute):
    total = entropy(rows)
    values = set(row[attribute] for row in rows)
    remainder = 0

    for value in values:
        subset = [row for row in rows if row[attribute] == value]
        remainder += len(subset) / len(rows) * entropy(subset)

    return total - remainder


def id3(rows, attributes):
    labels = [row[TARGET] for row in rows]

    if len(set(labels)) == 1:
        return labels[0]

    if not attributes:
        return Counter(labels).most_common(1)[0][0]

    best = max(attributes, key=lambda a: information_gain(rows, a))
    tree = {best: {}}

    for value in sorted(set(row[best] for row in rows)):
        subset = [row for row in rows if row[best] == value]
        remaining = [a for a in attributes if a != best]
        tree[best][value] = id3(subset, remaining)

    return tree


def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree

    attribute = next(iter(tree))
    value = sample[attribute]

    if value not in tree[attribute]:
        return "Unknown"

    return predict(tree[attribute][value], sample)


def show_tree(tree, indent=""):
    if not isinstance(tree, dict):
        print(indent + "-> " + tree)
        return

    attribute = next(iter(tree))
    for value, subtree in tree[attribute].items():
        print(indent + attribute + " = " + value)
        show_tree(subtree, indent + "  ")


tree = id3(data, ATTRIBUTES)

print("Decision Tree:")
show_tree(tree)

sample = {
    "Outlook": "Sunny",
    "Temperature": "Cool",
    "Humidity": "Normal",
    "Wind": "Strong"
}

print("\\nNew sample:", sample)
print("Predicted class:", predict(tree, sample))
