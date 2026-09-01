from collections import Counter, defaultdict
import re

# Training data
train = [
    ("team won cricket match", "Sports"),
    ("player scored century", "Sports"),
    ("cricket team played well", "Sports"),
    ("government passed new bill", "Politics"),
    ("minister announced policies", "Politics"),
    ("parliament discussed bill", "Politics")
]

# Test data
test = [
    ("cricket team won", "Sports"),
    ("government passed bill", "Politics"),
    ("player scored goal", "Sports"),
    ("minister announced bill", "Politics")
]

# Count classes, words and total words
classes = Counter(label for text, label in train)
words = defaultdict(Counter)
total_words = Counter()

for text, label in train:
    for word in re.findall(r'\w+', text.lower()):
        words[label][word] += 1
        total_words[label] += 1

vocab = set(word for text, label in train
            for word in re.findall(r'\w+', text.lower()))

# Prediction function
def predict(text):
    scores = {}

    for label in classes:
        score = classes[label] / len(train)

        for word in re.findall(r'\w+', text.lower()):
            score *= (words[label][word] + 1) / \
                     (total_words[label] + len(vocab))

        scores[label] = score

    return max(scores, key=scores.get)

# Predictions
actual = []
predicted = []

for text, label in test:
    p = predict(text)
    actual.append(label)
    predicted.append(p)
    print(text, "=>", p)

# Calculate TP, TN, FP, FN
TP = sum(a == "Sports" and p == "Sports"
         for a, p in zip(actual, predicted))

TN = sum(a == "Politics" and p == "Politics"
         for a, p in zip(actual, predicted))

FP = sum(a == "Politics" and p == "Sports"
         for a, p in zip(actual, predicted))

FN = sum(a == "Sports" and p == "Politics"
         for a, p in zip(actual, predicted))

# Evaluation metrics
accuracy = (TP + TN) / len(test)
precision = TP / (TP + FP) if TP + FP else 0
recall = TP / (TP + FN) if TP + FN else 0

print("\nTP =", TP, "TN =", TN, "FP =", FP, "FN =", FN)
print("Accuracy =", accuracy)
print("Precision =", precision)
print("Recall =", recall)
